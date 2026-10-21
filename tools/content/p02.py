"""p02 — Not insects."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, MC, TF, MATCH, write_chapter
from sources import src

S = ["TJ", "UMN-ARTH", "ENC-ARK", "WTK"]
R = lambda *c: [T(*x) if isinstance(x, tuple) else x for x in c]
chapter = {"id": "p02", "num": 2, "stage": 1, "kind": "lesson",
 "title": T("哪些不是昆虫", "What is not an insect", "Yang bukan serangga"),
 "blurb": T("蜘蛛、蜱、蜈蚣、马陆和弹尾虫：常被误认的节肢动物", "Spiders, ticks, centipedes, millipedes and springtails: arthropods often mistaken for insects", "Labah-labah, sengkenit, lipan, ulat gonggok dan ekor pegas: artropod yang sering disangka serangga"),
 "sources": S,
 "sections": [
 {"id": "s1", "heading": T("节肢动物大家族", "The arthropod family", "Keluarga artropod"), "level": "basic", "blocks": [
  P("{{t:arthropod}}是身体分节、有外骨骼、脚也分节的动物。昆虫只是其中一群；蜘蛛、蜈蚣、马陆、虾蟹也是节肢动物，但不是昆虫。",
    "An {{t:arthropod}} is an animal with a segmented body, an exoskeleton and jointed legs. Insects are one group of them; spiders, centipedes, millipedes, prawns and crabs are arthropods too, but not insects.",
    "{{t:arthropod}} ialah haiwan dengan badan beruas, rangka luar dan kaki bersendi. Serangga hanyalah satu kumpulannya; labah-labah, lipan, ulat gonggok, udang dan ketam juga artropod, tetapi bukan serangga.",
    defines=["arthropod"], src=["TJ:20", "TJ:22", "UMN-ARTH"]),
  {"type": "table", "src": ["TJ:22", "UMN-ARTH", "WTK:10"], "defines": ["arachnid"],
   "caption": T("数脚和看身体分区，就能分开它们", "Count the legs and the body parts to tell them apart", "Kira kaki dan bahagian badan untuk membezakannya"),
   "headers": R(("类群", "Group", "Kumpulan"), ("脚", "Legs", "Kaki"), ("身体分区", "Body parts", "Bahagian badan"), ("例子", "Examples", "Contoh")),
   "rows": [
    R(("昆虫", "Insects", "Serangga"), ("6 只", "6", "6"), ("3：头、胸、腹", "3: head, thorax, abdomen", "3: kepala, toraks, abdomen"), ("蝴蝶、甲虫、蚂蚁", "Butterflies, beetles, ants", "Rama-rama, kumbang, semut")),
    R(("{{t:arachnid}}", "{{t:arachnid}}", "{{t:arachnid}}"), ("8 只", "8", "8"), ("2：头胸部、腹部", "2: cephalothorax, abdomen", "2: sefalotoraks, abdomen"), ("蜘蛛、蜱、蝎子", "Spiders, ticks, scorpions", "Labah-labah, sengkenit, kala jengking")),
    R(("蜈蚣", "Centipedes", "Lipan"), ("每节 1 对", "1 pair per segment", "1 pasang setiap ruas"), ("头 + 许多体节", "Head + many segments", "Kepala + banyak ruas"), ("蜈蚣", "Centipedes", "Lipan")),
    R(("马陆", "Millipedes", "Ulat gonggok"), ("每节 2 对", "2 pairs per segment", "2 pasang setiap ruas"), ("头 + 许多体节", "Head + many segments", "Kepala + banyak ruas"), ("马陆", "Millipedes", "Ulat gonggok")),
    R(("甲壳动物", "Crustaceans", "Krustasia"), ("很多对", "Many pairs", "Banyak pasang"), ("多为头胸部、腹部", "Usually cephalothorax, abdomen", "Biasanya sefalotoraks, abdomen"), ("虾、蟹、鼠妇", "Prawns, crabs, woodlice", "Udang, ketam, kutu kayu"))]},
  N("tip", "蜱常被当成小甲虫。数一数：成年的蜱有四对、八只脚，所以属于蛛形纲，不是昆虫。",
    "Ticks are often taken for small beetles. Count the legs: an adult tick has four pairs, eight legs, so it is an arachnid, not an insect.",
    "Sengkenit sering disangka kumbang kecil. Kira kakinya: sengkenit dewasa mempunyai empat pasang, lapan kaki, jadi ia araknid, bukan serangga.",
    src=["WTK:10", "UMN-ARTH"]),
 ]},
 {"id": "s2", "heading": T("六只脚，却不是昆虫", "Six legs, but not insects", "Enam kaki, tetapi bukan serangga"), "level": "basic", "blocks": [
  P("{{t:springtail}}、原尾虫和双尾虫都有六只脚，过去被算作昆虫。它们的口器藏在头里面，现在归为{{t:hexapod}}，但不属于昆虫纲。",
    "{{t:springtail|Springtails}}, proturans and diplurans all have six legs and used to be counted as insects. Their mouthparts sit inside the head, and today they are classed as {{t:hexapod|hexapods}} but not as insects.",
    "{{t:springtail|Ekor pegas}}, protura dan diplura semuanya berkaki enam dan dahulu dikira sebagai serangga. Bahagian mulutnya terletak di dalam kepala, dan kini ia dikelaskan sebagai {{t:hexapod|heksapod}} tetapi bukan serangga.",
    defines=["springtail", "hexapod"], src=["TJ:22", "ENC-ARK"]),
  P("弹尾虫很小，通常只有 1–3 毫米，住在土壤和落叶里，帮助分解有机物。",
    "Springtails are tiny, usually 1–3 mm long, and live in soil and leaf litter, where they help break down dead plant matter.",
    "Ekor pegas sangat kecil, biasanya 1–3 mm panjang, dan hidup dalam tanah dan sarap daun, membantu mengurai bahan tumbuhan mati.",
    src=["WTK:10", "ENC-ARK"]),
 ]},
]}

terms = [
 ("arthropod", T("节肢动物", "Arthropod", "Artropod"), T("身体分节、有外骨骼和分节的脚的动物，包括昆虫、蜘蛛、蜈蚣和虾蟹。", "An animal with a segmented body, exoskeleton and jointed legs: insects, spiders, centipedes, crabs.", "Haiwan dengan badan beruas, rangka luar dan kaki bersendi: serangga, labah-labah, lipan, ketam.")),
 ("arachnid", T("蛛形纲动物", "Arachnid", "Araknid"), T("有八只脚、身体分两部分的节肢动物，如蜘蛛、蜱、蝎子。", "An arthropod with eight legs and a two-part body: spiders, ticks, scorpions.", "Artropod berkaki lapan dengan badan dua bahagian: labah-labah, sengkenit, kala jengking.")),
 ("springtail", T("弹尾虫", "Springtail", "Ekor pegas"), T("土壤里很小的六足动物，不属于昆虫纲。", "A tiny six-legged soil animal that is not an insect.", "Haiwan tanah berkaki enam yang sangat kecil dan bukan serangga.")),
 ("hexapod", T("六足动物", "Hexapod", "Heksapod"), T("所有六只脚的节肢动物：昆虫，加上弹尾虫、原尾虫和双尾虫。", "All six-legged arthropods: insects plus springtails, proturans and diplurans.", "Semua artropod berkaki enam: serangga serta ekor pegas, protura dan diplura.")),
]

quiz = [
 MC(T("蜘蛛有几只脚？", "How many legs does a spider have?", "Berapa kaki labah-labah?"), [T("6", "6", "6"), T("8", "8", "8"), T("10", "10", "10")], 1,
    T("蜘蛛是蛛形纲动物，有八只脚。", "Spiders are arachnids, with eight legs.", "Labah-labah ialah araknid, berkaki lapan."), ["TJ:22", "UMN-ARTH"]),
 MC(T("下面哪一种是昆虫？", "Which of these is an insect?", "Yang manakah serangga?"), [T("蜘蛛", "Spider", "Labah-labah"), T("蜈蚣", "Centipede", "Lipan"), T("蚂蚁", "Ant", "Semut"), T("马陆", "Millipede", "Ulat gonggok")], 2,
    T("蚂蚁有六只脚和三个体区。", "Ants have six legs and three body parts.", "Semut mempunyai enam kaki dan tiga bahagian badan."), ["TJ:22"]),
 TF(T("弹尾虫有六只脚，所以是昆虫。", "Springtails have six legs, so they are insects.", "Ekor pegas berkaki enam, jadi ia serangga."), False,
    T("弹尾虫是六足动物，但不属于昆虫纲。", "Springtails are hexapods but not insects.", "Ekor pegas ialah heksapod tetapi bukan serangga."), ["TJ:22", "ENC-ARK"]),
 MATCH(T("把动物和它的脚配对。", "Match each animal to its legs.", "Padankan haiwan dengan kakinya."),
    [(T("蜈蚣", "Centipede", "Lipan"), T("每节一对脚", "One pair per segment", "Sepasang setiap ruas")),
     (T("马陆", "Millipede", "Ulat gonggok"), T("每节两对脚", "Two pairs per segment", "Dua pasang setiap ruas")),
     (T("蜱", "Tick", "Sengkenit"), T("八只脚", "Eight legs", "Lapan kaki"))],
    T("蜈蚣每节一对脚，马陆每节两对，蜱是八只脚的蛛形纲动物。", "Centipedes: one pair per segment; millipedes: two; ticks: eight legs.", "Lipan: sepasang setiap ruas; ulat gonggok: dua; sengkenit: lapan kaki."), ["UMN-ARTH", "WTK:10"]),
]

write_chapter(chapter, terms, src(*S), quiz)
