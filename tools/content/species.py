"""Helper for stage 5 species pages and crop overviews."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, T2, P, L, N, SPECIES, PHOTO, CONTROL, write_chapter
from sources import src

NO_PHOTO = N("tip", "暂无合适的开放授权照片。", "No suitable openly licensed photo yet.", "Belum ada foto berlesen terbuka yang sesuai.", src=["TJ"])


def species_page(num, tid, names, sci, order, crops, stage, short, ident, ident_src,
                 role_heading, role_blocks, controls=(), photos=(), lookalike=None, quiz=(), authority=None,
                 blurb=None, notes=()):
    """controls: CONTROL blocks in IPM order. role_blocks: damage (pests) or role (helpers)."""
    cid = f"p{num:02d}"
    s1 = [SPECIES(names, sci, order, crops, stage, ident_src, authority=authority),
          *(PHOTO(p) for p in photos)]
    if not photos:
        s1.append(N("tip", "暂无合适的开放授权照片。", "No suitable openly licensed photo yet.", "Belum ada foto berlesen terbuka yang sesuai.", src=["TJ"]))
    s1.append(P("{{t:" + tid + "}}的辨认要点：", "How to recognise {{t:" + tid + "}}:", "Cara mengecam {{t:" + tid + "}}:", defines=[tid], src=ident_src))
    s1.append(L(*ident, src=ident_src))
    s1.extend(notes)
    sections = [{"id": "s1", "heading": T("认识它", "Recognising it", "Mengecamnya"), "level": "basic", "blocks": s1},
                {"id": "s2", "heading": role_heading, "level": "basic", "blocks": list(role_blocks)}]
    if lookalike:
        sections.append({"id": "s3", "heading": T("容易混淆", "Look-alikes", "Mudah dikelirukan"), "level": "basic", "blocks": list(lookalike)})
    if controls:
        sections.append({"id": "s4", "heading": T("防治方法", "Managing it", "Cara mengawal"), "level": "basic", "blocks": list(controls)})
    used = set()
    for sec in sections:
        for b in sec["blocks"]:
            for s in b.get("src", []):
                used.add(s.split(":")[0])
    for q in quiz:
        for s in q["src"]:
            used.add(s.split(":")[0])
    title = {"zh": f"{names['zh']}", "en": names["en"], "ms": names["ms"]}
    if names.get("zhTw"):
        title["zhTw"] = names["zhTw"]
    chapter = {"id": cid, "num": num, "stage": 5, "kind": "species", "order": order, "title": title,
               "blurb": blurb or T(sci, sci, sci), "sources": sorted(used), "sections": sections}
    write_chapter(chapter, [(tid, names, short)], src(*used), list(quiz))


def overview_page(num, title, blurb, blocks, quiz, links_heading=None):
    cid = f"p{num:02d}"
    sections = [{"id": "s1", "heading": T("概况", "Overview", "Gambaran"), "level": "basic", "blocks": list(blocks)}]
    used = set()
    for b in blocks:
        for s in b.get("src", []):
            used.add(s.split(":")[0])
    for q in quiz:
        for s in q["src"]:
            used.add(s.split(":")[0])
    chapter = {"id": cid, "num": num, "stage": 5, "kind": "crop", "title": title, "blurb": blurb, "sources": sorted(used), "sections": sections}
    write_chapter(chapter, [], src(*used), list(quiz))
