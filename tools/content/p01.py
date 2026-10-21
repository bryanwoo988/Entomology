"""p01 — What is an insect?"""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, MC, TF, MATCH, write_chapter
from sources import src

S = ["TJ"]
chapter = {"id": "p01", "num": 1, "stage": 1, "kind": "lesson",
 "title": T("什么是昆虫", "What is an insect?", "Apakah serangga?"),
 "blurb": T("六只脚、三个体区，以及怎样一眼认出昆虫", "Six legs, three body parts, and how to tell an insect at a glance", "Enam kaki, tiga bahagian badan, dan cara mengecam serangga sepintas lalu"),
 "sources": S,
 "sections": [
 {"id": "s1", "heading": T("昆虫的三个记号", "Three signs of an insect", "Tiga tanda serangga"), "level": "basic", "blocks": [
  P("{{t:insect}}是一类节肢动物：身体由许多节组成，外面包着一层坚硬的{{t:exoskeleton}}。在所有无脊椎动物里，只有昆虫会飞。",
    "An {{t:insect}} is a kind of arthropod: its body is made of many segments and wrapped in a hard {{t:exoskeleton}}. Of all animals without a backbone, only insects can fly.",
    "{{t:insect}} ialah sejenis artropod: badannya terdiri daripada banyak ruas dan dibalut oleh {{t:exoskeleton}} yang keras. Antara semua haiwan tanpa tulang belakang, hanya serangga yang boleh terbang.",
    defines=["insect", "exoskeleton"], src=["TJ:20", "TJ:31"]),
  P("要判断一只成年的小动物是不是昆虫，看这三件事：",
    "To tell whether an adult creature is an insect, check three things:",
    "Untuk mengetahui sama ada haiwan dewasa itu serangga, semak tiga perkara:",
    src=["TJ:20-21"]),
  L(("六只脚（三对）：最容易看的特征", "Six legs (three pairs): the easiest feature to check", "Enam kaki (tiga pasang): ciri yang paling mudah disemak"),
    ("身体分成{{t:head}}、{{t:thorax}}、{{t:abdomen}}三部分", "A body in three parts: {{t:head}}, {{t:thorax}} and {{t:abdomen}}", "Badan tiga bahagian: {{t:head}}, {{t:thorax}} dan {{t:abdomen}}"),
    ("多数成虫有两对翅；有些只有一对，有些没有翅", "Most adults have two pairs of wings; some have one pair, some none", "Kebanyakan dewasa mempunyai dua pasang sayap; ada yang sepasang, ada yang tiada"),
    defines=["head", "thorax", "abdomen"], src=["TJ:20-21", "TJ:31"]),
  N("tip", "这个方法只适用于成虫。毛虫、蛆这些幼虫的样子和成虫很不一样。",
    "This works for adults only. Larvae such as caterpillars and maggots look very different from their adults.",
    "Kaedah ini untuk serangga dewasa sahaja. Larva seperti ulat dan berenga kelihatan sangat berbeza daripada dewasanya.",
    src=["TJ:20"]),
  N("myth", "有些蝴蝶看起来只有四只脚。其实它们的前足退化得很小，收在身体前面，仍然是六只脚的昆虫。",
    "Some butterflies seem to have only four legs. Their front legs are just very small and held against the body; they are still six-legged insects.",
    "Sesetengah rama-rama kelihatan berkaki empat. Sebenarnya kaki depannya sangat kecil dan dilipat rapat ke badan; ia tetap serangga berkaki enam.",
    src=["TJ:21"]),
 ]},
 {"id": "s2", "heading": T("三个体区各管什么", "What each part does", "Tugas setiap bahagian"), "level": "basic", "blocks": [
  {"type": "keyval", "src": ["TJ:25", "TJ:29", "TJ:33"], "rows": [
   {"k": T("头部", "Head", "Kepala"), "v": T("感觉与取食的中心：触角、眼睛和口器都在这里", "The centre for senses and feeding: antennae, eyes and mouthparts", "Pusat deria dan makan: sesungut, mata dan bahagian mulut")},
   {"k": T("胸部", "Thorax", "Toraks"), "v": T("运动的中心：三对足和翅都长在这里", "The centre for movement: all three pairs of legs and the wings", "Pusat pergerakan: tiga pasang kaki dan sayap")},
   {"k": T("腹部", "Abdomen", "Abdomen"), "v": T("消化和生殖器官所在的地方", "Holds the digestive and reproductive organs", "Menempatkan organ pencernaan dan pembiakan")}]},
  P("点一下图上的部位，看看它叫什么、在哪一页讲解。",
    "Tap a part of the drawing to see its name and where it is explained.",
    "Ketik bahagian lukisan untuk melihat namanya dan di mana ia diterangkan.",
    src=["TJ:20-21"]),
  {"type": "widget", "id": "anatomy"},
 ]},
 {"id": "s3", "heading": T("昆虫有多少种", "How many kinds of insects?", "Berapa banyak jenis serangga?"), "level": "basic", "blocks": [
  P("世界上已知的昆虫超过一百万种，比其他所有动物加起来还多，占已知物种的一半以上。从高山到海边的潮间带，到处都有昆虫。",
    "More than a million kinds of insects are known, more than all other animals put together and over half of all known species. They live almost everywhere, from mountains to the seashore.",
    "Lebih sejuta jenis serangga telah diketahui, lebih banyak daripada semua haiwan lain digabungkan dan lebih separuh daripada semua spesies yang diketahui. Serangga hidup hampir di mana-mana, dari gunung hingga ke pantai.",
    src=["TJ:22"]),
 ]},
]}

terms = [
 ("insect", T("昆虫", "Insect", "Serangga"), T("身体分头、胸、腹三部分，有六只脚的节肢动物。", "An arthropod with a three-part body and six legs.", "Artropod dengan badan tiga bahagian dan enam kaki.")),
 ("exoskeleton", T("外骨骼", "Exoskeleton", "Rangka luar"), T("包在身体外面的坚硬外壳，支撑和保护身体。", "The hard outer casing that supports and protects the body.", "Kulit luar yang keras yang menyokong dan melindungi badan.")),
 ("head", T("头部", "Head", "Kepala"), T("昆虫身体的第一部分，有触角、眼睛和口器。", "The first body part, carrying the antennae, eyes and mouthparts.", "Bahagian pertama badan, dengan sesungut, mata dan bahagian mulut.")),
 ("thorax", T("胸部", "Thorax", "Toraks"), T("昆虫身体的中段，长着三对足和翅。", "The middle body part, carrying the three pairs of legs and the wings.", "Bahagian tengah badan, dengan tiga pasang kaki dan sayap.")),
 ("abdomen", T("腹部", "Abdomen", "Abdomen"), T("昆虫身体的最后一段，有消化和生殖器官。", "The last body part, holding the digestive and reproductive organs.", "Bahagian akhir badan, menempatkan organ pencernaan dan pembiakan.")),
]

quiz = [
 MC(T("成年昆虫有几只脚？", "How many legs does an adult insect have?", "Berapa kaki serangga dewasa?"),
    [T("4", "4", "4"), T("6", "6", "6"), T("8", "8", "8"), T("很多", "Many", "Banyak")], 1,
    T("昆虫有三对、共六只脚。", "Insects have three pairs: six legs.", "Serangga mempunyai tiga pasang: enam kaki."), ["TJ:20"]),
 TF(T("所有成年昆虫都有两对翅。", "Every adult insect has two pairs of wings.", "Setiap serangga dewasa mempunyai dua pasang sayap."), False,
    T("有些只有一对翅（如蝇），有些没有翅（如蚂蚁工蚁）。", "Some have one pair (flies) and some none (worker ants).", "Ada yang sepasang (lalat) dan ada yang tiada (semut pekerja)."), ["TJ:31", "TJ:38"]),
 MATCH(T("把体区和它的工作配对。", "Match each body part to its job.", "Padankan bahagian badan dengan tugasnya."),
    [(T("头部", "Head", "Kepala"), T("感觉与取食", "Senses and feeding", "Deria dan makan")),
     (T("胸部", "Thorax", "Toraks"), T("运动", "Movement", "Pergerakan")),
     (T("腹部", "Abdomen", "Abdomen"), T("消化与生殖", "Digestion and reproduction", "Pencernaan dan pembiakan"))],
    T("头部负责感觉和取食，胸部负责运动，腹部负责消化和生殖。", "Head: senses and feeding; thorax: movement; abdomen: digestion and reproduction.", "Kepala: deria dan makan; toraks: pergerakan; abdomen: pencernaan dan pembiakan."), ["TJ:25", "TJ:29", "TJ:33"]),
]

write_chapter(chapter, terms, src(*S), quiz)
