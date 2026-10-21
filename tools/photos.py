#!/usr/bin/env python3
"""Add a photo to the app: convert it, size it and register its credit.

    python3 tools/photos.py add <image> --id <id> \\
        --subject-zh … --subject-en … --subject-ms … \\
        --licence <MPOB-permission|own|CC0|CC BY 4.0|CC BY-SA 4.0|…> \\
        --author <name> --url <where it came from> \\
        [--source RS34 --issue 34 --year 2018] [--dry-run]

Writes img/species/<id>.webp (longest side at most 1200 px, never upscaled,
quality 80, no metadata) and upserts the entry in data/photos.json. With
--dry-run it prints the entry and writes nothing."""
import argparse
import json
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
LICENCES = ["MPOB-permission", "own", "PD", "CC0", "CC BY 2.0", "CC BY 3.0", "CC BY 3.0 US", "CC BY 4.0",
            "CC BY-SA 2.0", "CC BY-SA 3.0", "CC BY-SA 4.0"]
MAX_SIDE = 1200


def credit(a):
    if a.licence == "MPOB-permission":
        if not (a.issue and a.year):
            sys.exit("MPOB photos need --issue and --year")
        return {"zh": f"照片：马来西亚棕油局（MPOB），引自《Risalah Sawit》第 {a.issue} 期（{a.year}）",
                "en": f"Photo: Malaysian Palm Oil Board (MPOB), from Risalah Sawit No. {a.issue} ({a.year})",
                "ms": f"Foto: Lembaga Minyak Sawit Malaysia (MPOB), daripada Risalah Sawit Bil. {a.issue} ({a.year})"}
    if a.licence == "PD":
        return {"zh": f"照片：{a.author}，公有领域", "en": f"Photo: {a.author}, public domain", "ms": f"Foto: {a.author}, domain awam"}
    if a.licence == "own":
        return {"zh": f"照片：{a.author}", "en": f"Photo: {a.author}", "ms": f"Foto: {a.author}"}
    return {"zh": f"照片：{a.author}，{a.licence}", "en": f"Photo: {a.author}, {a.licence}", "ms": f"Foto: {a.author}, {a.licence}"}


def convert(src, dest):
    im = Image.open(src)
    im = im.convert("RGBA" if im.mode in ("RGBA", "LA", "P") else "RGB")
    if im.mode == "RGBA":
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[3])
        im = bg
    scale = min(1.0, MAX_SIDE / max(im.size))
    if scale < 1:
        im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    dest.parent.mkdir(parents=True, exist_ok=True)
    im.save(dest, "WEBP", quality=80, method=6)
    return im.size


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add")
    a.add_argument("image")
    a.add_argument("--id", required=True)
    for l in ("zh", "en", "ms"):
        a.add_argument(f"--subject-{l}", required=True)
    a.add_argument("--licence", required=True, choices=LICENCES)
    a.add_argument("--author", required=True)
    a.add_argument("--url", required=True)
    a.add_argument("--source")
    a.add_argument("--issue")
    a.add_argument("--year")
    a.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    entry = {"id": args.id, "file": f"img/species/{args.id}.webp",
             "subject": {"zh": args.subject_zh, "en": args.subject_en, "ms": args.subject_ms},
             "credit": credit(args), "licence": args.licence, "author": args.author, "url": args.url}
    if args.source:
        entry["source"] = args.source
    if args.dry_run:
        print(json.dumps(entry, ensure_ascii=False))
        return
    w, h = convert(args.image, ROOT / entry["file"])
    path = ROOT / "data" / "photos.json"
    photos = [p for p in json.loads(path.read_text()) if p["id"] != args.id] + [entry]
    path.write_text(json.dumps(sorted(photos, key=lambda p: p["id"]), ensure_ascii=False, indent=1) + "\n")
    size = (ROOT / entry["file"]).stat().st_size // 1024
    print(f"{entry['file']}  {w}x{h}  {size} KB")


if __name__ == "__main__":
    main()
