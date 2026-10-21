"""p04 — The thorax and legs."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, T2, P, L, N, MC, TF, MATCH, FIG, write_chapter
from sources import src

S = ["TJ", "PURDUE-TA"]
chapter = {"id": "p04", "num": 4, "stage": 1, "kind": "lesson",
 "title": T("胸部和足", "The thorax and legs", "Toraks dan kaki"),
 "blurb": T("三个胸节、足的六节，以及为跑、跳、挖、游、抓而变形的足", "Three thoracic segments, the six parts of a leg, and legs shaped for running, jumping, digging, swimming and grabbing", "Tiga ruas toraks, enam bahagian kaki, dan kaki yang berubah bentuk untuk berlari, melompat, menggali, berenang dan menangkap"),
 "sources": S,
 "sections": [
 {"id": "s1", "heading": T("运动的中心", "The centre of movement", "Pusat pergerakan"), "level": "basic", "blocks": [
  P("胸部由三节组成：{{t:prothorax}}、{{t:mesothorax}}和{{t:metathorax}}。每一节下面有一对足；翅长在中胸和后胸的背面。",
    "The thorax has three segments: the {{t:prothorax}}, {{t:mesothorax}} and {{t:metathorax}}. Each carries a pair of legs underneath; the wings grow from the top of the mesothorax and metathorax.",
    "Toraks mempunyai tiga ruas: {{t:prothorax}}, {{t:mesothorax}} dan {{t:metathorax}}. Setiap ruas mempunyai sepasang kaki di bawah; sayap tumbuh dari bahagian atas mesotoraks dan metatoraks.",
    defines=["prothorax", "mesothorax", "metathorax"], src=["TJ:29"]),
 ]},
 {"id": "s2", "heading": T("足的六个部分", "The six parts of a leg", "Enam bahagian kaki"), "level": "basic", "blocks": [
  P("从身体往外数，每只足有六个部分：",
    "Counting outwards from the body, each leg has six parts:",
    "Dikira dari badan ke luar, setiap kaki mempunyai enam bahagian:",
    src=["TJ:29"]),
  L(("{{t:coxa}}：连在身体上的第一节", "{{t:coxa}}: the first part, joined to the body", "{{t:coxa}}: bahagian pertama, bersambung dengan badan"),
    ("{{t:trochanter}}：很短的一小节", "{{t:trochanter}}: a short small part", "{{t:trochanter}}: bahagian kecil yang pendek"),
    ("{{t:femur}}：通常最粗壮的一节", "{{t:femur}}: usually the thickest part", "{{t:femur}}: biasanya bahagian paling tebal"),
    ("{{t:tibia}}：细长，常有刺", "{{t:tibia}}: long and thin, often spiny", "{{t:tibia}}: panjang dan halus, selalunya berduri"),
    ("{{t:tarsus}}：由几小节组成的脚掌", "{{t:tarsus}}: the 'foot', made of a few small segments", "{{t:tarsus}}: 'tapak kaki', terdiri daripada beberapa ruas kecil"),
    ("前跗节：最末端，带有{{t:claw}}", "Pretarsus: the very tip, with the {{t:claw|claws}}", "Pratarsus: hujung sekali, dengan {{t:claw|kuku}}"),
    ordered=True, defines=["coxa", "trochanter", "femur", "tibia", "tarsus", "claw"], src=["TJ:29"]),
  FIG("img/svg/fig-leg.svg", T("示意图：1 基节　2 转节　3 腿节　4 胫节　5 跗节　6 前跗节", "Drawing: 1 coxa, 2 trochanter, 3 femur, 4 tibia, 5 tarsus, 6 pretarsus", "Lukisan: 1 koksa, 2 trokanter, 3 femur, 4 tibia, 5 tarsus, 6 pratarsus"), T("示意图", "One leg with its six parts numbered", "Lukisan")),
 ]},
 {"id": "s3", "heading": T("变了形的足", "Legs shaped for a job", "Kaki yang berubah bentuk"), "level": "basic", "blocks": [
  P("足的形状告诉你这只昆虫怎样生活：",
    "The shape of the legs tells you how an insect lives:",
    "Bentuk kaki menunjukkan cara serangga itu hidup:",
    src=["TJ:29", "PURDUE-TA"]),
  FIG("img/svg/fig-legtypes.svg", T("示意图：1 步行足　2 跳跃足　3 捕捉足　4 挖掘足　5 游泳足", "Drawing: 1 walking or running, 2 jumping, 3 grasping, 4 digging, 5 swimming", "Lukisan: 1 berjalan atau berlari, 2 melompat, 3 penangkap, 4 penggali, 5 berenang"), T("示意图", "Five kinds of legs, numbered 1 to 5", "Lukisan")),
  {"type": "keyval", "src": ["TJ:29", "PURDUE-TA"], "defines": ["raptorial", "saltatorial", "fossorial"], "rows": [
   {"k": T("步行足", "Walking or running legs", "Kaki berjalan atau berlari"), "v": T("细长、各节差不多，适合快跑，如蟑螂", "Slender with similar parts, for running; cockroaches", "Langsing dengan bahagian serupa, untuk berlari; lipas")},
   {"k": T("{{t:saltatorial}}", "{{t:saltatorial|Jumping legs}}", "{{t:saltatorial|Kaki melompat}}"), "v": T("后足的腿节特别粗，如蝗虫", "Hind legs with a greatly enlarged femur; grasshoppers", "Kaki belakang dengan femur yang sangat besar; belalang")},
   {"k": T("{{t:raptorial}}", "{{t:raptorial|Grasping legs}}", "{{t:raptorial|Kaki penangkap}}"), "v": T("前足有刺，可以折起来夹住猎物，如螳螂", "Spiny front legs that fold shut on prey; mantids", "Kaki depan berduri yang dilipat untuk menangkap mangsa; cengkadak")},
   {"k": T("{{t:fossorial}}", "{{t:fossorial|Digging legs}}", "{{t:fossorial|Kaki penggali}}"), "v": T("前足宽扁像铲子，如蝼蛄", "Broad, flat front legs like spades; mole crickets", "Kaki depan lebar dan leper seperti penyodok; anjing tanah")},
   {"k": T("游泳足", "Swimming legs", "Kaki berenang"), "v": T("扁平、有长毛，像桨，如龙虱", "Flattened and fringed with hairs like oars; diving beetles", "Leper dan berbulu panjang seperti dayung; kumbang penyelam")}]},
  {"type": "gallery", "ids": ["mantis-hierodula", "mole-cricket-gryllotalpa", "grasshopper-tauchira"]},
 ]},
]}

terms = [
 ("prothorax", T("前胸", "Prothorax", "Protoraks"), T("胸部的第一节，长着前足。", "The first thoracic segment, carrying the front legs.", "Ruas toraks pertama, dengan kaki depan.")),
 ("mesothorax", T("中胸", "Mesothorax", "Mesotoraks"), T("胸部的第二节，长着中足和前翅。", "The second thoracic segment, with the middle legs and forewings.", "Ruas toraks kedua, dengan kaki tengah dan sayap depan.")),
 ("metathorax", T("后胸", "Metathorax", "Metatoraks"), T("胸部的第三节，长着后足和后翅。", "The third thoracic segment, with the hind legs and hind wings.", "Ruas toraks ketiga, dengan kaki belakang dan sayap belakang.")),
 ("coxa", T("基节", "Coxa", "Koksa"), T("足连在身体上的第一节。", "The leg segment joined to the body.", "Ruas kaki yang bersambung dengan badan.")),
 ("trochanter", T("转节", "Trochanter", "Trokanter"), T("基节和腿节之间的短小一节。", "The short segment between coxa and femur.", "Ruas pendek antara koksa dan femur.")),
 ("femur", T2("腿节", "腿节（股节）", "Femur", "Femur"), T("足上通常最粗壮的一节。", "Usually the thickest leg segment.", "Biasanya ruas kaki yang paling tebal.")),
 ("tibia", T("胫节", "Tibia", "Tibia"), T("腿节下面细长的一节。", "The long thin segment after the femur.", "Ruas panjang halus selepas femur.")),
 ("tarsus", T("跗节", "Tarsus", "Tarsus"), T("由几小节组成的脚掌部分。", "The 'foot', made of a few small segments.", "'Tapak kaki', terdiri daripada beberapa ruas kecil.")),
 ("claw", T("爪", "Claw", "Kuku"), T("足最末端的钩子，用来抓住物体。", "The hook at the tip of the leg, for gripping.", "Cangkuk di hujung kaki, untuk mencengkam.")),
 ("raptorial", T("捕捉足", "Raptorial (grasping) legs", "Kaki penangkap"), T("有刺、能夹住猎物的前足，如螳螂。", "Spiny front legs that seize prey, as in mantids.", "Kaki depan berduri untuk menangkap mangsa, seperti cengkadak.")),
 ("saltatorial", T("跳跃足", "Saltatorial (jumping) legs", "Kaki melompat"), T("腿节粗大、用来跳的后足，如蝗虫。", "Hind legs with a thick femur, for jumping, as in grasshoppers.", "Kaki belakang dengan femur tebal untuk melompat, seperti belalang.")),
 ("fossorial", T("挖掘足", "Fossorial (digging) legs", "Kaki penggali"), T("宽扁像铲子的前足，如蝼蛄。", "Broad spade-like front legs, as in mole crickets.", "Kaki depan lebar seperti penyodok, seperti anjing tanah.")),
]

quiz = [
 MC(T("螳螂的前足属于哪一种？", "What kind of front legs does a mantis have?", "Apakah jenis kaki depan cengkadak?"), [T("挖掘足", "Digging", "Penggali"), T("捕捉足", "Grasping", "Penangkap"), T("游泳足", "Swimming", "Berenang")], 1,
    T("螳螂的前足有刺，用来夹住猎物。", "A mantis's spiny front legs seize prey.", "Kaki depan cengkadak yang berduri menangkap mangsa."), ["TJ:29"]),
 TF(T("翅长在前胸上。", "Wings grow from the prothorax.", "Sayap tumbuh dari protoraks."), False,
    T("翅长在中胸和后胸。", "Wings grow from the mesothorax and metathorax.", "Sayap tumbuh dari mesotoraks dan metatoraks."), ["TJ:29"]),
 MC(T("蝗虫会跳，是因为后足哪一节特别粗？", "Grasshoppers jump because which part of the hind leg is enlarged?", "Belalang melompat kerana bahagian manakah kaki belakangnya membesar?"), [T("跗节", "Tarsus", "Tarsus"), T("腿节", "Femur", "Femur"), T("基节", "Coxa", "Koksa")], 1,
    T("跳跃足的腿节特别粗壮。", "Jumping legs have a greatly enlarged femur.", "Kaki melompat mempunyai femur yang sangat besar."), ["PURDUE-TA"]),
 MATCH(T("把足的类型和昆虫配对。", "Match the leg type to the insect.", "Padankan jenis kaki dengan serangga."),
    [(T("挖掘足", "Digging", "Penggali"), T("蝼蛄", "Mole cricket", "Anjing tanah")), (T("游泳足", "Swimming", "Berenang"), T("龙虱", "Diving beetle", "Kumbang penyelam")), (T("步行足", "Running", "Berlari"), T("蟑螂", "Cockroach", "Lipas"))],
    T("蝼蛄挖土、龙虱游泳、蟑螂快跑。", "Mole crickets dig, diving beetles swim, cockroaches run.", "Anjing tanah menggali, kumbang penyelam berenang, lipas berlari."), ["TJ:29", "PURDUE-TA"]),
]

write_chapter(chapter, terms, src(*S), quiz)
