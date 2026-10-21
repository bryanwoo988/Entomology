"""p06 — The abdomen."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, T2, P, L, N, MC, TF, MATCH, write_chapter
from sources import src

S = ["TJ", "PURDUE-TA"]
chapter = {"id": "p06", "num": 6, "stage": 1, "kind": "lesson",
 "title": T("腹部", "The abdomen", "Abdomen"),
 "blurb": T("气门、产卵器、尾须、尾铗和螫针", "Spiracles, ovipositor, cerci, forceps and sting", "Spirakel, ovipositor, serkus, penyepit dan sengat"),
 "sources": S,
 "sections": [
 {"id": "s1", "heading": T("消化与生殖", "Digestion and reproduction", "Pencernaan dan pembiakan"), "level": "basic", "blocks": [
  P("腹部装着消化和生殖器官，由许多环节组成，通常没有脚。",
    "The abdomen holds the digestive and reproductive organs. It is made of many ring-like segments and usually has no legs.",
    "Abdomen menempatkan organ pencernaan dan pembiakan. Ia terdiri daripada banyak ruas seperti cincin dan biasanya tiada kaki.",
    src=["TJ:33", "PURDUE-TA"]),
  P("身体两侧有一排小孔叫{{t:spiracle}}，空气从这里进入体内的气管。昆虫用气门呼吸，不是用嘴。",
    "Along each side is a row of small holes called {{t:spiracle|spiracles}}; air enters the breathing tubes through them. Insects breathe through spiracles, not through the mouth.",
    "Di sepanjang setiap sisi terdapat barisan lubang kecil dipanggil {{t:spiracle}}; udara masuk ke dalam salur pernafasan melaluinya. Serangga bernafas melalui spirakel, bukan melalui mulut.",
    defines=["spiracle"], src=["PURDUE-TA"]),
 ]},
 {"id": "s2", "heading": T("腹部末端的构造", "At the tip of the abdomen", "Di hujung abdomen"), "level": "basic", "blocks": [
  L(("{{t:ovipositor}}：雌虫产卵用的管子，螽斯的又长又像刀", "{{t:ovipositor}}: the female's egg-laying tube; long and blade-like in katydids", "{{t:ovipositor}}: tiub bertelur betina; panjang seperti bilah pada katidid"),
    ("{{t:cercus}}：一对细长的尾巴状附器", "{{t:cercus|Cerci}}: a pair of slender tail-like feelers", "{{t:cercus}}: sepasang tambahan halus seperti ekor"),
    ("尾铗：蠼螋腹末的一对钳子", "Forceps: the earwig's pair of pincers", "Penyepit: sepasang sepit di hujung abdomen cocopet"),
    ("螫针：蜂类的螫刺", "Sting: in bees and wasps", "Sengat: pada lebah dan tebuan"),
    ("攫握器：雄蜻蜓交配时抓住雌虫用", "Claspers: male dragonflies hold the female with them", "Pengapit: pepatung jantan memegang betina dengannya"),
    ("发音器：雄蝉腹部的鸣叫器官", "Sound organs: in the abdomen of male cicadas", "Organ bunyi: dalam abdomen riang-riang jantan"),
    defines=["ovipositor", "cercus"], src=["TJ:33"]),
  N("tip", "看到腹末有一对钳子，几乎一定是蠼螋；看到一根长长的“刀”，多半是雌螽斯。",
    "A pair of pincers at the tail almost always means an earwig; a long 'blade' usually means a female katydid.",
    "Sepasang sepit di hujung hampir pasti cocopet; 'bilah' panjang biasanya katidid betina.",
    src=["TJ:33", "TJ:40"]),
 ]},
]}

terms = [
 ("spiracle", T2("气门", "气孔", "Spiracle", "Spirakel"), T("身体两侧供空气进出的小孔。", "A small breathing hole along the side of the body.", "Lubang pernafasan kecil di sisi badan.")),
 ("ovipositor", T2("产卵器", "产卵管", "Ovipositor", "Ovipositor"), T("雌虫腹末用来产卵的管子。", "The female's egg-laying tube at the tip of the abdomen.", "Tiub bertelur betina di hujung abdomen.")),
 ("cercus", T2("尾须", "尾毛", "Cercus (pl. cerci)", "Serkus"), T("腹末一对细长的尾巴状附器。", "One of a pair of slender tail-like feelers at the tip of the abdomen.", "Salah satu sepasang tambahan halus seperti ekor di hujung abdomen.")),
]

quiz = [
 MC(T("腹末有一对钳子的是哪种昆虫？", "Which insect has a pair of pincers at its tail?", "Serangga manakah yang mempunyai sepasang sepit di ekornya?"), [T("蠼螋", "Earwig", "Cocopet"), T("蝗虫", "Grasshopper", "Belalang"), T("蜻蜓", "Dragonfly", "Pepatung")], 0,
    T("蠼螋的腹末有尾铗。", "Earwigs carry forceps at the tail.", "Cocopet mempunyai penyepit di ekor."), ["TJ:33"]),
 TF(T("昆虫通过身体两侧的气门呼吸。", "Insects breathe through spiracles along their sides.", "Serangga bernafas melalui spirakel di sisi badan."), True,
    T("空气从气门进入体内的气管。", "Air enters the breathing tubes through the spiracles.", "Udara masuk ke salur pernafasan melalui spirakel."), ["PURDUE-TA"]),
 MATCH(T("把构造和用途配对。", "Match each part to its use.", "Padankan bahagian dengan kegunaannya."),
    [(T2("产卵器", "产卵管", "Ovipositor", "Ovipositor"), T("产卵", "Laying eggs", "Bertelur")), (T2("气门", "气孔", "Spiracle", "Spirakel"), T("呼吸", "Breathing", "Bernafas")), (T("发音器", "Sound organ", "Organ bunyi"), T("雄蝉鸣叫", "A male cicada's song", "Nyanyian riang-riang jantan"))],
    T("产卵器产卵，气门呼吸，雄蝉用发音器鸣叫。", "Ovipositor: eggs; spiracles: breathing; sound organs: the cicada's song.", "Ovipositor: telur; spirakel: bernafas; organ bunyi: nyanyian riang-riang."), ["TJ:33", "PURDUE-TA"]),
]

write_chapter(chapter, terms, src(*S), quiz)
