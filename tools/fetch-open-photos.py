#!/usr/bin/env python3
"""Find openly licensed photos (CC0, CC BY, CC BY-SA) of a species.

    python3 tools/fetch-open-photos.py "Plutella xylostella" [more names…] [--out candidates.json] [--n 4]

Asks iNaturalist for research-grade observations whose photo licence allows
reuse, Malaysian observations first, for adults and for immature stages
(larva/nymph), falling back to observations with no life-stage label, then
Wikimedia Commons (CC0, CC BY, CC BY-SA, public domain), and prints candidates: image URL, licence, author, observation
link. Nothing is downloaded into the app; pick a photo, look at it, then add
it with tools/photos.py. One request per second; no personal data is sent."""
import argparse
import json
import time
import urllib.parse
import urllib.request

API = "https://api.inaturalist.org/v1/observations"
UA = {"User-Agent": "BugsApp-photo-survey/0.1"}
LICENCE = {"cc0": "CC0", "cc-by": "CC BY 4.0", "cc-by-sa": "CC BY-SA 4.0"}
STAGES = {"adult": "2", "larva": "6", "nymph": "5", "any": None}
COMMONS = "https://commons.wikimedia.org/w/api.php"
OK_COMMONS = ("CC0", "CC BY ", "CC BY-SA ", "Public domain")
MALAYSIA = 7155


def get(params):
    url = API + "?" + urllib.parse.urlencode(params)
    for i in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                time.sleep(1)
                return json.load(r)
        except Exception:
            time.sleep(3 * (i + 1))
    return {"results": []}


def candidates(name, stage, n):
    out, seen = [], set()
    for place in (MALAYSIA, None):
        q = {"taxon_name": name, "photo_license": "cc0,cc-by,cc-by-sa", "quality_grade": "research",
             "per_page": n, "order_by": "votes"}
        if STAGES[stage]:
            q.update(term_id=1, term_value_id=STAGES[stage])
        if place:
            q["place_id"] = place
        for o in get(q)["results"]:
            for p in o.get("photos", [])[:1]:
                code = p.get("license_code")
                if code not in LICENCE or p["id"] in seen:
                    continue
                seen.add(p["id"])
                out.append({"stage": stage, "malaysia": bool(place), "photo": p["url"].replace("square", "large"),
                            "licence": LICENCE[code], "author": (p.get("attribution") or "").split(",")[0].replace("(c) ", "").strip(),
                            "observation": f"https://www.inaturalist.org/observations/{o['id']}",
                            "taxon": o.get("taxon", {}).get("name")})
        if len(out) >= n:
            break
    return out[:n]


def commons(name, n):
    q = {"action": "query", "generator": "search", "gsrsearch": f'"{name}"', "gsrnamespace": 6, "gsrlimit": 20,
         "prop": "imageinfo", "iiprop": "url|extmetadata|mime", "format": "json"}
    url = COMMONS + "?" + urllib.parse.urlencode(q)
    pages = None
    for i in range(4):   # Commons rate-limits bursts: back off and retry
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                pages = json.load(r).get("query", {}).get("pages", {}).values()
            break
        except Exception:
            time.sleep(10 * (i + 1))
    if pages is None:
        return []
    time.sleep(3)
    out = []
    for p in pages:
        ii = (p.get("imageinfo") or [{}])[0]
        meta = ii.get("extmetadata", {})
        lic = meta.get("LicenseShortName", {}).get("value", "")
        if ii.get("mime") not in ("image/jpeg", "image/png") or not (lic in ("CC0", "Public domain") or lic.startswith(("CC BY ", "CC BY-SA "))):
            continue
        import re
        author = re.sub(r"<[^>]+>", "", meta.get("Artist", {}).get("value", "")).strip()
        out.append({"stage": "commons", "malaysia": False, "photo": ii.get("url"),
                    "licence": "PD" if lic == "Public domain" else lic, "author": author or "unknown",
                    "observation": ii.get("descriptionurl"), "taxon": name, "title": p.get("title")})
    return out[:n]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("names", nargs="+")
    ap.add_argument("--n", type=int, default=4)
    ap.add_argument("--out")
    a = ap.parse_args()
    found = {}
    for name in a.names:
        found[name] = [c for st in ("adult", "larva", "nymph") for c in candidates(name, st, a.n)]
        if not any(c["stage"] == "adult" for c in found[name]):
            found[name] += candidates(name, "any", a.n)
        if len(found[name]) < a.n:
            found[name] += commons(name, a.n * 2)
        print(f"{name}: " + ", ".join(f"{st} {sum(c['stage'] == st for c in found[name])}" for st in (*STAGES, "commons")))
    if a.out:
        with open(a.out, "w") as f:
            json.dump(found, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
