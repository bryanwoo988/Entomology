"""data/pesticides.json — every active ingredient named in a chemical control
block, with its status in Malaysia and where that was checked. Run before the
species pages."""
import json
import sys
sys.path.insert(0, 'tools/content')
from build import T, T2
from sources import SOURCES

P = [
 {"id": "cypermethrin", "name": T2("氯氰菊酯", "赛灭宁", "Cypermethrin", "Sipermetrin"), "status": "registered", "src": ["DOA-MRL"], "checked": "2026-10-21"},
 {"id": "lambda-cyhalothrin", "name": T2("高效氯氟氰菊酯", "赛洛宁", "Lambda-cyhalothrin", "Lambda-sihalotrin"), "status": "registered", "src": ["DOA-MRL"], "checked": "2026-10-21"},
 {"id": "carbofuran", "name": T2("克百威", "加保扶", "Carbofuran", "Karbofuran"), "status": "banned", "src": ["DOA-BAN", "DOA-CARBO"], "checked": "2026-10-21"},
]

if __name__ == "__main__":
    from pathlib import Path
    Path("data/pesticides.json").write_text(json.dumps(P, ensure_ascii=False, indent=1) + "\n")
    srcs = json.loads(Path("data/sources.json").read_text())
    by = {s["id"]: s for s in srcs}
    for p in P:
        for s in p["src"]:
            by[s] = {"id": s, **SOURCES[s]}
    Path("data/sources.json").write_text(json.dumps(sorted(by.values(), key=lambda s: s["id"]), ensure_ascii=False, indent=1) + "\n")
    print(f"{len(P)} active ingredients")
