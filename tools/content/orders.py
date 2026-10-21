"""Stage 4 — the insect orders (p10–p26), one page each from the data below.

Each order: name origin, key features, metamorphosis and mouthparts,
Malaysian examples, look-alikes, a memory aid, and at least three quiz items.
Farm species are linked from the species pages (and back) once they exist."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, T2, P, L, N, MC, TF, MATCH, write_chapter
from sources import src

FULL = T("完全变态（卵→幼虫→蛹→成虫）", "Complete (egg → larva → pupa → adult)", "Lengkap (telur → larva → pupa → dewasa)")
PART = T("不完全变态（卵→若虫→成虫）", "Incomplete (egg → nymph → adult)", "Tidak lengkap (telur → nimfa → dewasa)")
NONE = T("无变态（幼体像小成虫）", "None (young look like small adults)", "Tiada (anak seperti dewasa kecil)")
CHEW = T("咀嚼式", "Chewing", "Mengunyah")


# Malaysian examples (open-licence photos, credited on the page and in About).
GALLERY = {
 10: ["longhorn-pseudomyagrus", "scarab-ceroplophana", "oryctes-rhinoceros-adult"],
 11: ["butterfly-graphium-antiphates", "moth-brahmaea", "plutella-xylostella-larva"],
 12: ["cicada-trengganua", "assassin-bug-eulyes", "nilaparvata-lugens-adult"],
 13: ["carpenter-bee-xylocopa", "ant-polyrhachis", "apis-cerana-adult"],
 14: ["stalk-eyed-fly-teleopsis", "fruit-fly-euphranta", "bactrocera-carambolae-adult"],
 15: ["katydid-dicranopsyra", "leaf-grasshopper-chorotypus", "grasshopper-tauchira"],
 16: ["dragonfly-rhyothemis", "damselfly-rhinagrion"],
 17: ["orchid-mantis-hymenopus", "mantis-camelomantis"],
 18: ["cockroach-sundablatta", "termite-macrotermes-gilvus"],
 19: ["leaf-insect-pulchriphyllium", "stick-insect-marmessoidea"],
 20: ["thrips-scirtothrips", "thrips-parthenothrips"],
 21: ["earwig-forficula"],
 22: ["lacewing-mallada"],
 23: ["mayfly-atopopus"],
 24: ["caddisfly-macrostemum"],
 25: ["silverfish-ctenolepisma"],
 26: ["dobsonfly-protohermes", "stonefly-capnia", "scorpionfly-neopanorpa"],
}


def page(num, tid, name, term_short, etym, etym_src, features, feat_src, meta, mouth, meta_src,
         examples, ex_src, memory, quiz, compare=None, notes=(), blurb=None, extra_terms=()):
    cid = f"p{num:02d}"
    sci = name["en"].split(" (")[0]
    sections = [
     {"id": "s1", "heading": T("名字和特征", "Name and features", "Nama dan ciri"), "level": "basic", "blocks": [
       P(*etym, defines=[tid], src=etym_src),
       *([{"type": "gallery", "ids": GALLERY[num]}] if num in GALLERY else []),
       N("key", *memory, src=etym_src),
       L(*features, src=feat_src),
       *notes]},
     {"id": "s2", "heading": T("生活史和口器", "Life cycle and mouthparts", "Kitaran hidup dan bahagian mulut"), "level": "basic", "blocks": [
       {"type": "keyval", "src": meta_src, "rows": [
         {"k": T("发育", "Development", "Perkembangan"), "v": meta},
         {"k": T("口器", "Mouthparts", "Bahagian mulut"), "v": mouth}]}]},
     {"id": "s3", "heading": T("马来西亚常见的", "Common in Malaysia", "Biasa di Malaysia"), "level": "basic", "blocks": [
       L(*examples, src=ex_src)]},
    ]
    if compare:
        sections.append({"id": "s4", "heading": compare["heading"], "level": "basic", "blocks": compare["blocks"]})
    chapter = {"id": cid, "num": num, "stage": 4, "kind": "order",
               "title": T(f"{name['zh']}", name["en"], name["ms"]) if "zhTw" not in name else name,
               "blurb": blurb or T(name["zh"], name["en"], name["ms"]),
               "sources": sorted({s.split(":")[0] for b in [*etym_src, *feat_src, *meta_src, *ex_src] for s in [b]}), "sections": sections}
    used = set(chapter["sources"])
    for sec in sections:
        for b in sec["blocks"]:
            for s in b.get("src", []):
                used.add(s.split(":")[0])
    for q in quiz:
        for s in q["src"]:
            used.add(s.split(":")[0])
    chapter["sources"] = sorted(used)
    write_chapter(chapter, [(tid, name, term_short), *extra_terms], src(*used), quiz)


Y = lambda zh, en, ms: (zh, en, ms)

# ---------------------------------------------------------------- p10 Coleoptera
page(10, "coleoptera", T("鞘翅目（甲虫）", "Coleoptera (beetles)", "Coleoptera (kumbang)"),
 T("甲虫所属的目：前翅硬化成鞘翅。", "The beetle order: forewings hardened into elytra.", "Order kumbang: sayap depan mengeras menjadi elitra."),
 Y("{{t:coleoptera}}的名字来自希腊文 koleos（鞘）加 pteron（翅），意思是「有鞘的翅」：甲虫坚硬的前翅像刀鞘一样，把后翅收在里面。",
   "{{t:coleoptera}} comes from the Greek koleos (sheath) and pteron (wing): 'sheath-winged'. A beetle's hard forewings cover the hind wings like a sheath.",
   "{{t:coleoptera}} berasal daripada bahasa Yunani koleos (sarung) dan pteron (sayap): 'bersayap sarung'. Sayap depan kumbang yang keras menutupi sayap belakang seperti sarung."),
 ["ETYM"],
 [Y("前翅硬化成鞘翅，两片在背中线对齐", "Forewings hardened into elytra that meet in a straight line down the back", "Sayap depan mengeras menjadi elitra yang bertemu dalam garis lurus di belakang"),
  Y("膜质的后翅折叠在鞘翅下面", "Membranous hind wings folded under the elytra", "Sayap belakang bermembran dilipat di bawah elitra"),
  Y("咀嚼式口器", "Chewing mouthparts", "Bahagian mulut mengunyah")],
 ["WTK:1", "TJ:40", "UMN-ORD"], FULL, CHEW, ["TJ:35", "UMN-ORD"],
 [Y("叶甲、瓢虫、犀角金龟、萤火虫", "Leaf beetles, ladybirds, rhinoceros beetles, fireflies", "Kumbang daun, kumbang kura-kura, kumbang badak, kelip-kelip")], ["WTK:1"],
 Y("「鞘」就是刀鞘：硬翅像刀鞘一样包住后翅。", "Think 'sheath': hard covers sheathing the flying wings.", "Ingat 'sarung': penutup keras menyarungi sayap terbang."),
 [MC(T("Coleoptera 这个名字是什么意思？", "What does Coleoptera mean?", "Apakah maksud Coleoptera?"), [T("鳞片翅", "Scale wing", "Sayap bersisik"), T("有鞘的翅", "Sheath wing", "Sayap bersarung"), T("一半的翅", "Half wing", "Separuh sayap")], 1,
     T("koleos 是鞘，pteron 是翅。", "Koleos is sheath; pteron is wing.", "Koleos ialah sarung; pteron ialah sayap."), ["ETYM"]),
  TF(T("甲虫是完全变态的昆虫。", "Beetles have complete metamorphosis.", "Kumbang mengalami metamorfosis lengkap."), True,
     T("甲虫经过卵、幼虫、蛹、成虫四个阶段。", "Egg, larva, pupa, adult.", "Telur, larva, pupa, dewasa."), ["TJ:35"]),
  MC(T("下面哪一种是甲虫？", "Which of these is a beetle?", "Yang manakah kumbang?"), [T("萤火虫", "Firefly", "Kelip-kelip"), T("蝉", "Cicada", "Riang-riang"), T("蟋蟀", "Cricket", "Cengkerik")], 0,
     T("萤火虫属于鞘翅目。", "Fireflies are beetles.", "Kelip-kelip ialah kumbang."), ["WTK:1"])],
 compare={"heading": T2("甲虫还是蝽？", "甲虫还是椿象？", "Beetle or bug?", "Kumbang atau pepijat?"), "blocks": [
  {"type": "table", "src": ["TJ:39", "TJ:40", "TJ:35"], "caption": T2("甲虫和蝽怎样分", "甲虫和椿象怎样分", "Telling beetles from true bugs", "Membezakan kumbang dan pepijat"),
   "headers": [T("比较", "Compare", "Banding"), T("甲虫", "Beetle", "Kumbang"), T2("蝽", "椿象", "True bug", "Pepijat")],
   "rows": [[T("前翅", "Forewings", "Sayap depan"), T("全部是硬壳，在背中线对齐", "Wholly hard, meeting in a straight line", "Keras sepenuhnya, bertemu dalam garis lurus"), T("前半硬、后半膜质，在背上交叠", "Hard at base, thin at tip, overlapping", "Keras di pangkal, nipis di hujung, bertindih")],
            [T("口器", "Mouth", "Mulut"), T("咀嚼式", "Chewing", "Mengunyah"), T("针管状刺吸式", "Needle-like beak", "Paruh seperti jarum")],
            [T("发育", "Development", "Perkembangan"), T("完全变态", "Complete", "Lengkap"), T("不完全变态", "Incomplete", "Tidak lengkap")]]}]})

# ---------------------------------------------------------------- p11 Lepidoptera
page(11, "lepidoptera", T("鳞翅目（蝶和蛾）", "Lepidoptera (butterflies and moths)", "Lepidoptera (rama-rama dan kupu-kupu)"),
 T("蝶和蛾所属的目：翅上盖满鳞片。", "The butterfly and moth order: wings covered in scales.", "Order rama-rama dan kupu-kupu: sayap diliputi sisik."),
 Y("{{t:lepidoptera}}来自希腊文 lepis（鳞片）加 pteron（翅），意思是「鳞片翅」。",
   "{{t:lepidoptera}} comes from the Greek lepis (scale) and pteron (wing): 'scale-winged'.",
   "{{t:lepidoptera}} berasal daripada bahasa Yunani lepis (sisik) dan pteron (sayap): 'bersayap sisik'."),
 ["ETYM"],
 [Y("两对翅盖满细小的鳞片，摸了会掉色粉", "Two pairs of wings covered in tiny scales that rub off as coloured dust", "Dua pasang sayap diliputi sisik halus yang tertanggal seperti debu berwarna"),
  Y("成虫的口器是一根卷起来的长吸管（虹吸式）", "Adults feed through a long coiled tube (siphoning)", "Dewasa makan melalui tiub panjang bergulung (menyedut)"),
  Y("幼虫是毛虫，用咀嚼式口器吃叶子", "Larvae are caterpillars that chew leaves", "Larva ialah ulat yang mengunyah daun")],
 ["TJ:38", "TJ:27", "WTK:2", "UMN-ORD"], FULL,
 T("成虫虹吸式；幼虫咀嚼式", "Adults siphoning; larvae chewing", "Dewasa menyedut; larva mengunyah"), ["TJ:35", "TJ:27", "UMN-ORD"],
 [Y("蝴蝶：如粉蝶、蛱蝶、小灰蝶", "Butterflies: whites, brush-foots, blues", "Rama-rama: putih, kaki berus, biru"),
  Y("蛾：如灯蛾、夜蛾、袋蛾", "Moths: tiger moths, owlet moths, bagworms", "Kupu-kupu: kupu-kupu harimau, kupu-kupu malam, ulat bungkus"),
  Y("弄蝶：身体粗壮多毛", "Skippers: stout, hairy bodies", "Rama-rama skipper: badan tegap berbulu")], ["WTK:2", "TJ:43", "RS34"],
 Y("「鳞」就是鱼鳞：翅上盖满小鳞片。", "Think 'scales': wings tiled like a fish.", "Ingat 'sisik': sayap bersisik seperti ikan."),
 [MC(T("蝴蝶的触角是什么样子？", "What do butterfly antennae look like?", "Bagaimanakah rupa sesungut rama-rama?"), [T("末端膨大的棍棒状", "Clubbed at the tip", "Berbonjol di hujung"), T("像羽毛", "Feathery", "Berbulu pelepah"), T("像一串珠", "Bead-like", "Seperti manik")], 0,
     T("蝴蝶的触角细长，末端膨大。", "Butterfly antennae end in a club.", "Sesungut rama-rama berbonjol di hujung."), ["WTK:2"]),
  TF(T("毛虫是鳞翅目的幼虫。", "Caterpillars are the larvae of Lepidoptera.", "Ulat ialah larva Lepidoptera."), True,
     T("蝶和蛾的幼虫是毛虫。", "Butterfly and moth larvae are caterpillars.", "Larva rama-rama dan kupu-kupu ialah ulat."), ["UMN-ORD"]),
  MATCH(T("把触角和昆虫配对。", "Match the antennae to the insect.", "Padankan sesungut dengan serangga."),
     [(T("棍棒状", "Clubbed", "Berbonjol"), T("蝴蝶", "Butterfly", "Rama-rama")), (T("羽状或锯齿状", "Feathery or saw-edged", "Berbulu pelepah atau bergerigi"), T("蛾", "Moth", "Kupu-kupu")), (T("末端弯成钩", "Hooked at the tip", "Bercangkuk di hujung"), T("弄蝶", "Skipper", "Skipper"))],
     T("蝴蝶棍棒状，蛾羽状或锯齿状，弄蝶末端有钩。", "Butterflies: clubbed; moths: feathery or saw-edged; skippers: hooked.", "Rama-rama: berbonjol; kupu-kupu: berbulu atau bergerigi; skipper: bercangkuk."), ["WTK:2"])],
 compare={"heading": T("蝴蝶、蛾还是弄蝶？", "Butterfly, moth or skipper?", "Rama-rama, kupu-kupu atau skipper?"), "blocks": [
  {"type": "table", "src": ["WTK:2", "WTK:8"], "caption": T("先看触角", "Look at the antennae first", "Lihat sesungut dahulu"),
   "headers": [T("比较", "Compare", "Banding"), T("触角", "Antennae", "Sesungut"), T("身体", "Body", "Badan")],
   "rows": [[T("蝴蝶", "Butterfly", "Rama-rama"), T("细长，末端膨大", "Long, clubbed tip", "Panjang, hujung berbonjol"), T("较细", "Slender", "Langsing")],
            [T("蛾", "Moth", "Kupu-kupu"), T("羽状或锯齿状", "Feathery or saw-edged", "Berbulu pelepah atau bergerigi"), T("多较粗", "Often stout", "Selalunya tegap")],
            [T("弄蝶", "Skipper", "Skipper"), T("末端膨大后弯成钩", "Club bent into a hook", "Bonjol bengkok seperti cangkuk"), T("粗壮多毛", "Stout and hairy", "Tegap dan berbulu")],
            [T("石蛾（毛翅目）", "Caddisfly (Trichoptera)", "Lalat kadis (Trichoptera)"), T("细长如线，翅上是毛不是鳞", "Long thread-like; hairy, not scaly, wings", "Panjang seperti benang; sayap berbulu, bukan bersisik"), T("像蛾", "Moth-like", "Seperti kupu-kupu")]]}]})

# ---------------------------------------------------------------- p12 Hemiptera
page(12, "hemiptera", T("半翅目（蝽、蝉、蚜虫）", "Hemiptera (true bugs, cicadas, aphids)", "Hemiptera (pepijat, riang-riang, afid)"),
 T("用针管状口器吸汁的昆虫：蝽、蝉、叶蝉、飞虱、蚜虫等。", "Insects with a sucking beak: true bugs, cicadas, hoppers, aphids.", "Serangga dengan paruh penghisap: pepijat, riang-riang, bena, afid."),
 Y("{{t:hemiptera}}来自希腊文 hemi（一半）加 pteron（翅），指蝽的前翅一半硬、一半软。",
   "{{t:hemiptera}} comes from the Greek hemi (half) and pteron (wing), after the true bugs' forewings, half hard and half soft.",
   "{{t:hemiptera}} berasal daripada bahasa Yunani hemi (separuh) dan pteron (sayap), merujuk sayap depan pepijat yang separuh keras dan separuh lembut."),
 ["LSJ", "TJ:39"],
 [Y("针管状的刺吸式口器，平时收在头下", "A needle-like piercing-sucking beak, folded under the head", "Paruh menusuk-menghisap seperti jarum, dilipat di bawah kepala"),
  Y("蝽类：前翅前半硬、后半膜质（半鞘翅）", "True bugs: forewings hard at the base and membranous at the tip (hemelytra)", "Pepijat: sayap depan keras di pangkal dan bermembran di hujung (hemelitra)"),
  Y("蝉、叶蝉、飞虱、蚜虫：翅全部是膜质", "Cicadas, leafhoppers, planthoppers, aphids: wings wholly membranous", "Riang-riang, bena daun, bena perang, afid: sayap bermembran sepenuhnya"),
  Y("许多种类背上有一块三角形的小盾片", "Many have a triangular scutellum on the back", "Banyak mempunyai skutelum segi tiga di belakang")],
 ["TJ:39", "TJ:31", "WTK:1"], PART, T("刺吸式", "Piercing-sucking", "Menusuk-menghisap"), ["TJ:35", "TJ:39"],
 [Y("蝽、红蝽、缘蝽、猎蝽、臭虫", "Stink bugs, red bugs, squash bugs, assassin bugs, bed bugs", "Pepijat busuk, pepijat merah, pepijat labu, pepijat pembunuh, pepijat katil"),
  Y("水黾、仰泳蝽、划蝽", "Water striders, backswimmers, water boatmen", "Pepijat air, pepijat renang terbalik, pendayung air"),
  Y("蝉、叶蝉、飞虱、蚜虫", "Cicadas, leafhoppers, planthoppers, aphids", "Riang-riang, bena daun, bena perang, afid")], ["WTK:1", "TJ:39"],
 Y("「半」就是一半：前翅一半硬、一半软；口器像针管。", "Think 'half': half-hard forewings, and a straw for a mouth.", "Ingat 'separuh': sayap depan separuh keras, dan mulut seperti straw."),
 [MC(T("半翅目的口器是哪一种？", "What mouthparts do Hemiptera have?", "Apakah bahagian mulut Hemiptera?"), [T("咀嚼式", "Chewing", "Mengunyah"), T("刺吸式", "Piercing-sucking", "Menusuk-menghisap"), T("虹吸式", "Siphoning", "Menyedut")], 1,
     T("半翅目用针管状口器刺吸汁液。", "Hemiptera pierce and suck with a beak.", "Hemiptera menusuk dan menghisap dengan paruh."), ["TJ:39"]),
  TF(T("蝉和蚜虫属于半翅目。", "Cicadas and aphids belong to Hemiptera.", "Riang-riang dan afid tergolong dalam Hemiptera."), True,
     T("它们和蝽一样有刺吸式口器，只是翅全部是膜质。", "Like true bugs they have a sucking beak; their wings are wholly membranous.", "Seperti pepijat, ia mempunyai paruh penghisap; sayapnya bermembran sepenuhnya."), ["TJ:39"]),
  MC(T("哪一种是半翅目的害虫？", "Which pest belongs to Hemiptera?", "Perosak manakah tergolong dalam Hemiptera?"), [T("飞虱", "Planthopper", "Bena perang"), T("毛虫", "Caterpillar", "Ulat"), T("犀角金龟", "Rhinoceros beetle", "Kumbang badak")], 0,
     T("飞虱用刺吸式口器吸稻株汁液。", "Planthoppers suck rice sap with their beak.", "Bena perang menghisap cecair padi dengan paruhnya."), ["TJ:39"])],
 notes=[N("tip", "以前把蝉、叶蝉、蚜虫分成「同翅目」，现在都归入半翅目。", "Cicadas, hoppers and aphids used to be split off as 'Homoptera'; today they are all part of Hemiptera.", "Riang-riang, bena dan afid dahulu diasingkan sebagai 'Homoptera'; kini semuanya sebahagian daripada Hemiptera.", src=["TJ:39"])])

# ---------------------------------------------------------------- p13 Hymenoptera
page(13, "hymenoptera", T("膜翅目（蜂和蚂蚁）", "Hymenoptera (bees, wasps and ants)", "Hymenoptera (lebah, tebuan dan semut)"),
 T("蜂和蚂蚁所属的目：两对膜质翅，有细腰。", "The bee, wasp and ant order: two pairs of membranous wings and a narrow waist.", "Order lebah, tebuan dan semut: dua pasang sayap bermembran dan pinggang sempit."),
 Y("{{t:hymenoptera}}来自希腊文 hymen（薄膜）加 pteron（翅），意思是「膜翅」，由林奈命名。",
   "{{t:hymenoptera}} comes from the Greek hymen (membrane) and pteron (wing): 'membrane-winged'. Linnaeus coined it.",
   "{{t:hymenoptera}} berasal daripada bahasa Yunani hymen (membran) dan pteron (sayap): 'bersayap membran'. Linnaeus mencipta nama ini."),
 ["ETYM"],
 [Y("两对透明的膜质翅", "Two pairs of clear membranous wings", "Dua pasang sayap bermembran yang jernih"),
  Y("胸和腹之间有明显的细腰", "A clear narrow waist between thorax and abdomen", "Pinggang sempit yang jelas antara toraks dan abdomen"),
  Y("蚂蚁的腰上有一两个结，触角膝状", "Ants have one or two nodes on the waist and elbowed antennae", "Semut mempunyai satu atau dua nod pada pinggang dan sesungut bersiku"),
  Y("蜂类腹末有螫针", "Bees and wasps have a sting at the tip of the abdomen", "Lebah dan tebuan mempunyai sengat di hujung abdomen")],
 ["TJ:39", "TJ:38", "TJ:33", "WTK:3"], FULL, T("咀嚼式或嚼吸式", "Chewing or chewing-lapping", "Mengunyah atau mengunyah-menjilat"), ["TJ:35", "TJ:27"],
 [Y("蜜蜂（包括东方蜜蜂）", "Honey bees, including the Asian honey bee", "Lebah madu, termasuk lebah madu Asia"),
  Y("胡蜂、黄蜂", "Wasps and hornets", "Tebuan dan penyengat"),
  Y("蚂蚁", "Ants", "Semut")], ["WTK:3", "TJ:212"],
 Y("「膜」就是薄膜：四片透明的翅，加一条细腰。", "Think 'membrane': four clear wings and a wasp waist.", "Ingat 'membran': empat sayap jernih dan pinggang tebuan."),
 [MC(T("怎样分辨有翅的蚂蚁和有翅的白蚁？", "How do you tell a winged ant from a winged termite?", "Bagaimana membezakan semut bersayap daripada anai-anai bersayap?"), [T("蚂蚁有细腰、触角膝状", "Ants have a narrow waist and elbowed antennae", "Semut mempunyai pinggang sempit dan sesungut bersiku"), T("蚂蚁的翅比较大", "Ants have bigger wings", "Semut mempunyai sayap lebih besar"), T("白蚁有螫针", "Termites have stings", "Anai-anai mempunyai sengat")], 0,
     T("白蚁触角念珠状、没有细腰。", "Termites have bead-like antennae and no waist.", "Anai-anai mempunyai sesungut seperti manik dan tiada pinggang."), ["TJ:38", "TJ:39"]),
  TF(T("膜翅目是完全变态的昆虫。", "Hymenoptera have complete metamorphosis.", "Hymenoptera mengalami metamorfosis lengkap."), True,
     T("蜂和蚂蚁有卵、幼虫、蛹、成虫四个阶段。", "Egg, larva, pupa, adult.", "Telur, larva, pupa, dewasa."), ["TJ:35"]),
  MC(T("Hymenoptera 的 hymen 是什么意思？", "What does 'hymen' in Hymenoptera mean?", "Apakah maksud 'hymen' dalam Hymenoptera?"), [T("薄膜", "Membrane", "Membran"), T("蜂蜜", "Honey", "Madu"), T("细腰", "Waist", "Pinggang")], 0,
     T("hymen 是薄膜，pteron 是翅。", "Hymen is membrane; pteron is wing.", "Hymen ialah membran; pteron ialah sayap."), ["ETYM"])],
 compare={"heading": T("蚂蚁还是白蚁？", "Ant or termite?", "Semut atau anai-anai?"), "blocks": [
  {"type": "table", "src": ["TJ:38", "TJ:39"], "caption": T("看触角和腰", "Look at the antennae and the waist", "Lihat sesungut dan pinggang"),
   "headers": [T("比较", "Compare", "Banding"), T("蚂蚁", "Ant", "Semut"), T("白蚁", "Termite", "Anai-anai")],
   "rows": [[T("触角", "Antennae", "Sesungut"), T("膝状", "Elbowed", "Bersiku"), T("念珠状", "Bead-like", "Seperti manik")],
            [T("腰", "Waist", "Pinggang"), T("细，有结", "Narrow, with nodes", "Sempit, ada nod"), T("没有细腰", "No waist", "Tiada pinggang")],
            [T("有翅繁殖蚁", "Winged swarmers", "Kelekatu"), T("前后翅大小不同", "Fore- and hind wings differ", "Sayap depan dan belakang berbeza"), T("四翅几乎一样大", "Four nearly equal wings", "Empat sayap hampir sama besar")]]}]})

# ---------------------------------------------------------------- p14 Diptera
page(14, "diptera", T("双翅目（蝇和蚊）", "Diptera (flies and mosquitoes)", "Diptera (lalat dan nyamuk)"),
 T("蝇和蚊所属的目：只有一对翅，后翅变成平衡棒。", "The fly order: one pair of wings, the hind pair reduced to halteres.", "Order lalat: sepasang sayap, sayap belakang menjadi halter."),
 Y("{{t:diptera}}来自希腊文 di（二）加 pteron（翅），意思是「两片翅」：它们只有一对能飞的翅。",
   "{{t:diptera}} comes from the Greek di (two) and pteron (wing): 'two-winged'. Flies have just one pair of flying wings.",
   "{{t:diptera}} berasal daripada bahasa Yunani di (dua) dan pteron (sayap): 'bersayap dua'. Lalat hanya mempunyai sepasang sayap untuk terbang."),
 ["LSJ"],
 [Y("只有一对前翅，后翅变成一对平衡棒", "Only one pair of forewings; the hind wings are a pair of halteres", "Hanya sepasang sayap depan; sayap belakang menjadi sepasang halter"),
  Y("蝇、虻的触角短；蚊、蠓的触角细长多节", "Flies have short antennae; mosquitoes and midges have long many-segmented ones", "Lalat mempunyai sesungut pendek; nyamuk dan agas mempunyai sesungut panjang berbilang ruas"),
  Y("身体多半有毛", "Body usually hairy", "Badan biasanya berbulu")],
 ["TJ:38", "WTK:6"], T("完全变态，幼虫是蛆", "Complete; larvae are maggots", "Lengkap; larva ialah berenga"),
 T("舐吸式（如家蝇、果实蝇）或刺吸式（如蚊）", "Sponging (house flies, fruit flies) or piercing-sucking (mosquitoes)", "Menyerap (lalat rumah, lalat buah) atau menusuk-menghisap (nyamuk)"), ["TJ:35", "TJ:27", "UMN-ORD", "NCSU-META"],
 [Y("家蝇、实蝇、食蚜蝇", "House flies, fruit flies, hoverflies", "Lalat rumah, lalat buah, lalat bunga"),
  Y("大蚊、马蝇、牛虻、蜂虻、食虫虻", "Crane flies, bot flies, horse flies, bee flies, robber flies", "Lalat kren, lalat bot, langau, lalat lebah, lalat perompak"),
  Y("蚊、瘿蚊", "Mosquitoes and gall midges", "Nyamuk dan agas gal")], ["WTK:6", "TJ:43"],
 Y("「双」就是两片：只有两片翅，后面两根小棒帮它平衡。", "Think 'two': two wings, plus two tiny knobs for balance.", "Ingat 'dua': dua sayap, dan dua tombol kecil untuk keseimbangan."),
 [MC(T("蝇的后翅变成了什么？", "What have a fly's hind wings become?", "Sayap belakang lalat telah menjadi apa?"), [T("鞘翅", "Elytra", "Elitra"), T("平衡棒", "Halteres", "Halter"), T("鳞片", "Scales", "Sisik")], 1,
     T("双翅目的后翅变成平衡棒。", "Diptera hind wings are halteres.", "Sayap belakang Diptera ialah halter."), ["TJ:38"]),
  TF(T("马蝇像蜜蜂，但不会螫人。", "Horse bot flies look like bees but cannot sting.", "Lalat bot kuda seperti lebah tetapi tidak boleh menyengat."), True,
     T("它们只有一对翅，没有螫针。", "They have one pair of wings and no sting.", "Ia bersayap sepasang dan tiada sengat."), ["WTK:6"]),
  MC(T("蚊的触角是什么样子？", "What are a mosquito's antennae like?", "Bagaimanakah sesungut nyamuk?"), [T("很短", "Very short", "Sangat pendek"), T("细长多节", "Long and many-segmented", "Panjang berbilang ruas"), T("像一串珠", "Bead-like", "Seperti manik")], 1,
     T("蚊属于长角亚目，触角细长。", "Mosquitoes have long antennae.", "Nyamuk mempunyai sesungut panjang."), ["TJ:38"])],
 compare={"heading": T("蜂还是像蜂的蝇？", "Bee, or a fly that looks like one?", "Lebah, atau lalat yang menyerupainya?"), "blocks": [
  P("有些蝇长得像蜂。数翅就知道：蜂有两对翅，蝇只有一对，后面多两根小棒；蝇也没有螫针。",
    "Some flies mimic bees. Count the wings: bees have two pairs; flies have one, with two tiny knobs behind, and no sting.",
    "Sesetengah lalat menyerupai lebah. Kira sayapnya: lebah ada dua pasang; lalat ada sepasang dengan dua tombol kecil di belakang, dan tiada sengat.",
    src=["TJ:38", "WTK:6"])]})

# ---------------------------------------------------------------- p15 Orthoptera
page(15, "orthoptera", T("直翅目（蝗虫、螽斯、蟋蟀）", "Orthoptera (grasshoppers, katydids, crickets)", "Orthoptera (belalang, katidid, cengkerik)"),
 T("后足善跳的昆虫：蝗虫、螽斯、蟋蟀、蝼蛄。", "Jumping insects: grasshoppers, katydids, crickets, mole crickets.", "Serangga pelompat: belalang, katidid, cengkerik, anjing tanah."),
 Y("{{t:orthoptera}}来自希腊文 orthos（直）加 pteron（翅），意思是「直的翅」：前翅窄长而直。",
   "{{t:orthoptera}} comes from the Greek orthos (straight) and pteron (wing): 'straight-winged', after the long narrow forewings.",
   "{{t:orthoptera}} berasal daripada bahasa Yunani orthos (lurus) dan pteron (sayap): 'bersayap lurus', merujuk sayap depan yang panjang dan sempit."),
 ["LSJ"],
 [Y("后足是粗大的跳跃足", "Hind legs are big jumping legs", "Kaki belakang ialah kaki melompat yang besar"),
  Y("前翅像皮革（覆翅）", "Leathery forewings (tegmina)", "Sayap depan seperti kulit (tegmina)"),
  Y("很多种类会摩擦身体发声", "Many make sounds by rubbing body parts together", "Banyak menghasilkan bunyi dengan menggesel bahagian badan")],
 ["WTK:5", "TJ:40", "PURDUE-TA", "TJ:30"], PART, CHEW, ["TJ:35", "UMN-ORD"],
 [Y("蝗虫，如霹雳州拍到的「猴蝗」", "Grasshoppers, such as the monkey grasshopper photographed in Perak", "Belalang, seperti belalang monyet yang dirakam di Perak"),
  Y("模仿叶子的蝗虫 Systella rafflesii 和拟叶螽", "Leaf-mimicking grasshoppers (Systella rafflesii) and leaf katydids (Pseudophyllinae)", "Belalang penyamar daun (Systella rafflesii) dan katidid daun (Pseudophyllinae)"),
  Y("蟋蟀，如雪兰莪州的卷叶蟋蟀；蝼蛄", "Crickets, such as the leaf-rolling cricket in Selangor; mole crickets", "Cengkerik, seperti cengkerik penggulung daun di Selangor; anjing tanah")], ["WTK:5", "TJ:75"],
 Y("「直」：窄长的直翅，加上会跳的后腿。", "Think 'straight': long straight wings and jumping hind legs.", "Ingat 'lurus': sayap lurus panjang dan kaki belakang pelompat."),
 [MC(T("蝗虫和螽斯最容易用什么分开？", "What best tells a grasshopper from a katydid?", "Apakah cara terbaik membezakan belalang dan katidid?"), [T("触角长短", "Antenna length", "Panjang sesungut"), T("颜色", "Colour", "Warna"), T("脚的数目", "Number of legs", "Bilangan kaki")], 0,
     T("螽斯、蟋蟀触角细长；蝗虫触角短粗。", "Katydids and crickets have long thin antennae; grasshoppers short thick ones.", "Katidid dan cengkerik bersesungut panjang halus; belalang pendek tebal."), ["TJ:40", "WTK:5"]),
  TF(T("蝼蛄的前足是挖掘足。", "A mole cricket's front legs are digging legs.", "Kaki depan anjing tanah ialah kaki penggali."), True,
     T("蝼蛄用铲状前足挖土。", "Mole crickets dig with spade-like front legs.", "Anjing tanah menggali dengan kaki depan seperti penyodok."), ["TJ:75"]),
  MC(T("直翅目是哪一种发育方式？", "How do Orthoptera develop?", "Bagaimana Orthoptera berkembang?"), [T("不完全变态", "Incomplete metamorphosis", "Metamorfosis tidak lengkap"), T("完全变态", "Complete metamorphosis", "Metamorfosis lengkap"), T("无变态", "No metamorphosis", "Tanpa metamorfosis")], 0,
     T("直翅目：卵、若虫、成虫。", "Egg, nymph, adult.", "Telur, nimfa, dewasa."), ["TJ:35"])],
 compare={"heading": T2("蝗虫还是螽斯？", "蝗虫还是螽蟴？", "Grasshopper or katydid?", "Belalang atau katidid?"), "blocks": [
  {"type": "table", "src": ["TJ:40", "WTK:5", "TJ:33"], "caption": T("看触角和发声方法", "Look at the antennae and how they sing", "Lihat sesungut dan cara berbunyi"),
   "headers": [T("比较", "Compare", "Banding"), T("蝗虫", "Grasshopper", "Belalang"), T2("螽斯、蟋蟀", "螽蟴、蟋蟀", "Katydid, cricket", "Katidid, cengkerik")],
   "rows": [[T("触角", "Antennae", "Sesungut"), T("短而粗", "Short and thick", "Pendek dan tebal"), T("细长，常比身体还长", "Thin, often longer than the body", "Halus, sering lebih panjang daripada badan")],
            [T("发声", "Sound", "Bunyi"), T("后足的齿列刮前翅", "Pegs on the hind legs rubbed against the wings", "Pasak pada kaki belakang digesel pada sayap"), T("两片前翅互相摩擦", "Rubbing the forewings together", "Menggesel kedua-dua sayap depan")],
            [T("身体", "Body", "Badan"), T("较细长", "Slimmer", "Lebih langsing"), T("较圆胖，有的像叶子", "Rounder, some leaf-like", "Lebih bulat, ada yang seperti daun")]]}]})

# ---------------------------------------------------------------- p16 Odonata
page(16, "odonata", T2("蜻蜓目（蜻蜓、豆娘）", "蜻蛉目（蜻蜓、豆娘）", "Odonata (dragonflies and damselflies)", "Odonata (pepatung dan pepatung jarum)"),
 T("蜻蜓和豆娘：大眼、短触角、两对翅，幼虫在水中。", "Dragonflies and damselflies: big eyes, tiny antennae, two pairs of wings, young in water.", "Pepatung: mata besar, sesungut pendek, dua pasang sayap, anak dalam air."),
 Y("{{t:odonata}}来自希腊文 odous（牙齿），指它们有齿的大颚。它们是空中的捕食者。",
   "{{t:odonata}} comes from the Greek odous (tooth), after their toothed jaws. They are hunters of the air.",
   "{{t:odonata}} berasal daripada bahasa Yunani odous (gigi), merujuk rahangnya yang bergigi. Ia pemburu di udara."),
 ["LSJ"],
 [Y("复眼很大，触角短得几乎看不见", "Huge compound eyes; tiny bristle-like antennae", "Mata majmuk sangat besar; sesungut sangat pendek"),
  Y("两对膜质翅，翅脉很密", "Two pairs of membranous, densely veined wings", "Dua pasang sayap bermembran dengan urat yang padat"),
  Y("若虫（稚虫）在水中生活", "The nymphs (naiads) live in water", "Nimfa (naiad) hidup dalam air")],
 ["TJ:27", "TJ:39", "WTK:3", "TJ:35"], PART, CHEW, ["TJ:35", "UMN-ORD"],
 [Y("蜻蜓", "Dragonflies", "Pepatung"), Y("豆娘", "Damselflies", "Pepatung jarum")], ["WTK:3"],
 Y("「牙齿」：有齿的大颚，空中的猎人。", "Think 'tooth': toothed jaws, a hunter on the wing.", "Ingat 'gigi': rahang bergigi, pemburu di udara."),
 [MC(T("停下时把翅合起在背上的通常是？", "Which usually rests with its wings closed over the back?", "Yang manakah biasanya berehat dengan sayap tertutup?"), [T("豆娘", "Damselfly", "Pepatung jarum"), T("蜻蜓", "Dragonfly", "Pepatung")], 0,
     T("豆娘停下时多合起翅，蜻蜓平展翅。", "Damselflies close their wings; dragonflies hold them out.", "Pepatung jarum menutup sayap; pepatung membentangkannya."), ["INAT-ODO", "TJ:39"]),
  TF(T("蜻蜓的若虫在水中生活。", "Dragonfly nymphs live in water.", "Nimfa pepatung hidup dalam air."), True,
     T("水生的若虫叫稚虫。", "Water-dwelling nymphs are called naiads.", "Nimfa akuatik dipanggil naiad."), ["TJ:35"]),
  MC(T("蜻蜓的两眼通常？", "A dragonfly's eyes usually…", "Mata pepatung biasanya…"), [T("在头顶相接或几乎相接", "Meet or nearly meet on top of the head", "Bertemu atau hampir bertemu di atas kepala"), T("分得很开", "Are widely separated", "Berjauhan")], 0,
     T("豆娘两眼分开，蜻蜓两眼相接。", "Damselflies' eyes are far apart; dragonflies' meet.", "Mata pepatung jarum berjauhan; mata pepatung bertemu."), ["INAT-ODO"])],
 compare={"heading": T("蜻蜓还是豆娘？", "Dragonfly or damselfly?", "Pepatung atau pepatung jarum?"), "blocks": [
  {"type": "table", "src": ["TJ:39", "INAT-ODO"], "caption": T("看翅和眼", "Look at the wings and eyes", "Lihat sayap dan mata"),
   "headers": [T("比较", "Compare", "Banding"), T("蜻蜓", "Dragonfly", "Pepatung"), T("豆娘", "Damselfly", "Pepatung jarum")],
   "rows": [[T("翅", "Wings", "Sayap"), T("后翅基部较宽", "Hind wings broader at the base", "Sayap belakang lebih lebar di pangkal"), T("四片翅差不多", "Four similar wings", "Empat sayap serupa")],
            [T("停下时", "At rest", "Ketika berehat"), T("翅向两侧平展", "Wings held out flat", "Sayap terbentang"), T("翅多合起在背上", "Wings mostly closed over the back", "Sayap kebanyakannya tertutup")],
            [T("眼", "Eyes", "Mata"), T("相接或几乎相接", "Touching or nearly so", "Bertemu atau hampir"), T("分得很开", "Widely separated", "Berjauhan")]]}]})

# ---------------------------------------------------------------- p17 Mantodea
page(17, "mantodea", T("螳螂目", "Mantodea (mantids)", "Mantodea (cengkadak)"),
 T("螳螂：前足是有刺的捕捉足。", "Mantids: spiny grasping front legs.", "Cengkadak: kaki depan penangkap yang berduri."),
 Y("{{t:mantodea}}的 mantis 在希腊文里是「先知」，大概因为螳螂举起前足，好像在祈祷。",
   "The 'mantis' in {{t:mantodea}} is Greek for 'prophet', perhaps because a mantis holds up its front legs as if praying.",
   "'Mantis' dalam {{t:mantodea}} bermaksud 'nabi' dalam bahasa Yunani, mungkin kerana cengkadak mengangkat kaki depannya seolah-olah berdoa."),
 ["LSJ"],
 [Y("前足是有刺的捕捉足，可以夹住猎物", "Spiny grasping front legs that seize prey", "Kaki depan penangkap berduri yang menangkap mangsa"),
  Y("前翅像皮革（覆翅）", "Leathery forewings (tegmina)", "Sayap depan seperti kulit (tegmina)"),
  Y("捕食其他昆虫", "Hunts other insects", "Memburu serangga lain")],
 ["TJ:29", "TJ:40", "PURDUE-TA"], PART, CHEW, ["TJ:35", "UMN-ORD"],
 [Y("各种绿色、褐色的螳螂", "Green and brown praying mantids", "Cengkadak hijau dan perang")], ["WTK:6"],
 Y("「祈祷」：举起带刺的前足，等猎物上门。", "Think 'praying': spiny front legs raised, waiting for prey.", "Ingat 'berdoa': kaki depan berduri diangkat, menunggu mangsa."),
 [MC(T("螳螂的前足叫什么？", "What are a mantis's front legs called?", "Apakah nama kaki depan cengkadak?"), [T("捕捉足", "Grasping legs", "Kaki penangkap"), T("跳跃足", "Jumping legs", "Kaki melompat"), T("游泳足", "Swimming legs", "Kaki berenang")], 0,
     T("螳螂的前足是捕捉足。", "Mantids have grasping front legs.", "Cengkadak mempunyai kaki depan penangkap."), ["TJ:29"]),
  TF(T("螳螂是不完全变态。", "Mantids have incomplete metamorphosis.", "Cengkadak mengalami metamorfosis tidak lengkap."), True,
     T("螳螂：卵、若虫、成虫。", "Egg, nymph, adult.", "Telur, nimfa, dewasa."), ["TJ:35"]),
  MC(T("螳螂吃什么？", "What do mantids eat?", "Apakah makanan cengkadak?"), [T("其他昆虫", "Other insects", "Serangga lain"), T("树叶", "Leaves", "Daun"), T("花蜜", "Nectar", "Nektar")], 0,
     T("螳螂是捕食者。", "Mantids are predators.", "Cengkadak ialah pemangsa."), ["TJ:29"])])

# ---------------------------------------------------------------- p18 Blattodea
page(18, "blattodea", T("蜚蠊目（蟑螂和白蚁）", "Blattodea (cockroaches and termites)", "Blattodea (lipas dan anai-anai)"),
 T("蟑螂和白蚁：白蚁其实是过群居生活的蟑螂。", "Cockroaches and termites: termites are social cockroaches.", "Lipas dan anai-anai: anai-anai ialah lipas yang hidup berkoloni."),
 Y("{{t:blattodea}}包括蟑螂和白蚁。以前白蚁自成一目（等翅目），分子研究证实白蚁其实是过群居生活的蟑螂，现在归入蜚蠊目。",
   "{{t:blattodea}} includes cockroaches and termites. Termites used to have their own order (Isoptera); molecular studies showed they are social cockroaches, and they now belong here.",
   "{{t:blattodea}} merangkumi lipas dan anai-anai. Anai-anai dahulu mempunyai ordernya sendiri (Isoptera); kajian molekul menunjukkan ia lipas yang hidup berkoloni, dan kini tergolong di sini."),
 ["INWARD2007"],
 [Y("蟑螂：前翅像皮革，脚是善跑的步行足", "Cockroaches: leathery forewings and running legs", "Lipas: sayap depan seperti kulit dan kaki berlari"),
  Y("白蚁：触角念珠状，没有细腰", "Termites: bead-like antennae and no narrow waist", "Anai-anai: sesungut seperti manik dan tiada pinggang sempit"),
  Y("有翅的白蚁四片翅几乎一样大，分飞后翅会脱落", "Winged termites have four nearly equal wings, shed after the swarm", "Anai-anai bersayap mempunyai empat sayap hampir sama besar, tertanggal selepas berkerumun")],
 ["PURDUE-TA", "TJ:38", "TJ:39", "WTK:4"], PART, CHEW, ["TJ:35", "UMN-ORD"],
 [Y("美洲大蠊、德国小蠊", "American and German cockroaches", "Lipas Amerika dan lipas Jerman"),
  Y("野外的斑马纹蟑螂、橙斑蟑螂，以及沙捞越的森林蟑螂", "Wild zebra-striped and orange-spotted cockroaches, and forest cockroaches in Sarawak", "Lipas liar berjalur zebra dan bertompok jingga, serta lipas hutan di Sarawak"),
  Y("白蚁的工蚁、兵蚁和有翅繁殖蚁", "Termite workers, soldiers and winged swarmers", "Anai-anai pekerja, askar dan kelekatu")], ["WTK:4"],
 Y("记住：白蚁是「会合作的蟑螂」，不是蚂蚁。", "Remember: termites are 'team-working cockroaches', not ants.", "Ingat: anai-anai ialah 'lipas yang bekerjasama', bukan semut."),
 [TF(T("白蚁和蚂蚁是近亲。", "Termites are close relatives of ants.", "Anai-anai ialah saudara dekat semut."), False,
     T("白蚁属于蜚蠊目，是蟑螂的近亲；蚂蚁属于膜翅目。", "Termites are Blattodea, related to cockroaches; ants are Hymenoptera.", "Anai-anai tergolong dalam Blattodea, saudara lipas; semut dalam Hymenoptera."), ["INWARD2007"]),
  MC(T("白蚁的触角是什么形状？", "What shape are termite antennae?", "Apakah bentuk sesungut anai-anai?"), [T("念珠状", "Bead-like", "Seperti manik"), T("膝状", "Elbowed", "Bersiku"), T("羽状", "Feathery", "Berbulu pelepah")], 0,
     T("白蚁的触角像一串珠。", "Termite antennae are bead-like.", "Sesungut anai-anai seperti manik."), ["TJ:38"]),
  MC(T("以前白蚁属于哪一目？", "Which order were termites placed in before?", "Dalam order manakah anai-anai diletakkan dahulu?"), [T("等翅目", "Isoptera", "Isoptera"), T("膜翅目", "Hymenoptera", "Hymenoptera"), T("直翅目", "Orthoptera", "Orthoptera")], 0,
     T("白蚁以前是等翅目，现在归入蜚蠊目。", "Termites were Isoptera; now they are Blattodea.", "Anai-anai dahulu Isoptera; kini Blattodea."), ["INWARD2007", "TJ:86"])])

# ---------------------------------------------------------------- p19 Phasmida
page(19, "phasmida", T("竹节虫目（竹节虫和叶䗛）", "Phasmida (stick and leaf insects)", "Phasmida (serangga ranting dan serangga daun)"),
 T("身体像树枝或叶子的植食性昆虫。", "Plant-eating insects that look like twigs or leaves.", "Serangga pemakan tumbuhan yang menyerupai ranting atau daun."),
 Y("{{t:phasmida}}来自希腊文 phasma（幻影），因为它们伪装得像树枝和叶子，好像会凭空消失。",
   "{{t:phasmida}} comes from the Greek phasma (apparition): they are so well disguised as twigs and leaves that they seem to vanish.",
   "{{t:phasmida}} berasal daripada bahasa Yunani phasma (bayangan): ia menyamar begitu baik sebagai ranting dan daun sehingga seolah-olah hilang."),
 ["LSJ"],
 [Y("身体细长像树枝，或扁平像叶子", "Body like a twig, or flat like a leaf", "Badan seperti ranting, atau leper seperti daun"),
  Y("脚细长，行动缓慢", "Long thin legs and slow movements", "Kaki panjang halus dan pergerakan perlahan"),
  Y("前足不是捕捉足（和螳螂不同）", "Front legs are not grasping legs (unlike mantids)", "Kaki depan bukan kaki penangkap (tidak seperti cengkadak)")],
 ["WTK:6", "TJ:40"], PART, CHEW, ["TJ:35", "UMN-ORD"],
 [Y("竹节虫：马来半岛已知约 136 种", "Stick insects: about 136 species are known from Peninsular Malaysia", "Serangga ranting: kira-kira 136 spesies diketahui di Semenanjung Malaysia"),
  Y("叶䗛，如灰叶䗛", "Leaf insects, such as the grey leaf insect", "Serangga daun, seperti serangga daun kelabu")], ["SEOW-PHASMID", "WTK:6"],
 Y("「幻影」：看得见的树枝，原来是一只虫。", "Think 'ghost': the twig you see is an insect.", "Ingat 'bayangan': ranting yang anda lihat ialah serangga."),
 [MC(T("Phasmida 的 phasma 是什么意思？", "What does 'phasma' mean?", "Apakah maksud 'phasma'?"), [T("幻影", "Apparition", "Bayangan"), T("树枝", "Twig", "Ranting"), T("叶子", "Leaf", "Daun")], 0,
     T("phasma 是幻影。", "Phasma means apparition.", "Phasma bermaksud bayangan."), ["LSJ"]),
  TF(T("竹节虫的前足是捕捉足。", "Stick insects have grasping front legs.", "Serangga ranting mempunyai kaki depan penangkap."), False,
     T("捕捉足是螳螂的特征。", "Grasping front legs belong to mantids.", "Kaki depan penangkap ialah ciri cengkadak."), ["TJ:40"]),
  MC(T("马来半岛已知的竹节虫大约有多少种？", "About how many stick insect species are known from Peninsular Malaysia?", "Kira-kira berapa spesies serangga ranting diketahui di Semenanjung Malaysia?"), [T("约 13 种", "About 13", "Kira-kira 13"), T("约 136 种", "About 136", "Kira-kira 136"), T("约 1360 种", "About 1,360", "Kira-kira 1,360")], 1,
     T("Seow-Choen（2021）记录约 136 种。", "Seow-Choen (2021) recognises about 136.", "Seow-Choen (2021) mengiktiraf kira-kira 136."), ["SEOW-PHASMID"])])

# ---------------------------------------------------------------- p20 Thysanoptera
page(20, "thysanoptera", T("缨翅目（蓟马）", "Thysanoptera (thrips)", "Thysanoptera (trips)"),
 T("蓟马：很小、细长，翅窄而有长缨毛。", "Thrips: tiny and slender, with narrow fringed wings.", "Trips: sangat kecil dan langsing, dengan sayap sempit berjumbai."),
 Y("{{t:thysanoptera}}来自希腊文 thysanos（流苏、缨）加 pteron（翅），指翅边缘的长毛。",
   "{{t:thysanoptera}} comes from the Greek thysanos (fringe) and pteron (wing), after the long hairs edging the wings.",
   "{{t:thysanoptera}} berasal daripada bahasa Yunani thysanos (jumbai) dan pteron (sayap), merujuk bulu panjang di tepi sayap."),
 ["LSJ"],
 [Y("体长只有约 1–2 毫米，细长，两头尖", "Only about 1–2 mm long, slender and tapered at both ends", "Hanya kira-kira 1–2 mm panjang, langsing dan tirus di kedua-dua hujung"),
  Y("翅很窄，边缘有很长的缨毛；只有成虫有翅", "Narrow wings fringed with long hairs; only adults have wings", "Sayap sempit berjumbai bulu panjang; hanya dewasa bersayap"),
  Y("口器左右不对称，用来刮破叶面吸汁", "Lopsided mouthparts that scrape leaf surfaces and suck the juice", "Bahagian mulut tidak simetri yang mengikis permukaan daun dan menghisap cecairnya")],
 ["UMD-THRIPS", "CSU-THRIPS"], PART, T("锉吸式（不对称）", "Rasping-sucking (asymmetrical)", "Mengikis-menghisap (tidak simetri)"), ["TJ:35", "CSU-THRIPS"],
 [Y("金马仑高原的茄子、辣椒和甜椒上，最多的是 Thrips palmi 和 Thrips parvispinus", "On eggplant, chilli and bell pepper in Cameron Highlands the commonest are Thrips palmi and Thrips parvispinus", "Pada terung, cili dan lada benggala di Cameron Highlands yang paling banyak ialah Thrips palmi dan Thrips parvispinus"),
  Y("它们吃叶、花和果实，也会传播植物病毒", "They feed on leaves, flowers and fruit, and also spread plant viruses", "Ia makan daun, bunga dan buah, dan juga menyebarkan virus tumbuhan")], ["SER-THRIPS"],
 Y("「缨」就是流苏：翅像镶了流苏的细羽毛。", "Think 'fringe': wings like tiny tasselled feathers.", "Ingat 'jumbai': sayap seperti bulu pelepah kecil berjumbai."),
 [MC(T("蓟马大约多大？", "About how big is a thrips?", "Kira-kira berapa besar trips?"), [T("1–2 毫米", "1–2 mm", "1–2 mm"), T("1–2 厘米", "1–2 cm", "1–2 cm"), T("5 厘米", "5 cm", "5 cm")], 0,
     T("成虫约 1–2 毫米，要用放大镜看。", "Adults are about 1–2 mm; use a hand lens.", "Dewasa kira-kira 1–2 mm; gunakan kanta pembesar."), ["UMD-THRIPS"]),
  TF(T("蓟马除了吃植物，还会传播植物病毒。", "Besides feeding, thrips can spread plant viruses.", "Selain makan, trips boleh menyebarkan virus tumbuhan."), True,
     T("金马仑的研究指出它们是病毒的传播者。", "The Cameron Highlands study notes they are virus vectors.", "Kajian Cameron Highlands menyatakan ia vektor virus."), ["SER-THRIPS"]),
  MC(T("蓟马翅的特点是？", "What is special about thrips wings?", "Apakah keistimewaan sayap trips?"), [T("边缘有长缨毛", "Fringed with long hairs", "Berjumbai bulu panjang"), T("盖满鳞片", "Covered in scales", "Diliputi sisik"), T("硬壳", "Hard shells", "Cangkerang keras")], 0,
     T("Thysanoptera 意思就是缨翅。", "Thysanoptera means fringe-winged.", "Thysanoptera bermaksud bersayap jumbai."), ["UMD-THRIPS", "LSJ"])])

# ---------------------------------------------------------------- p21 Dermaptera
page(21, "dermaptera", T("革翅目（蠼螋）", "Dermaptera (earwigs)", "Dermaptera (cocopet)"),
 T("蠼螋：腹末有一对钳子。", "Earwigs: a pair of pincers at the tail.", "Cocopet: sepasang penyepit di ekor."),
 Y("{{t:dermaptera}}来自希腊文 derma（皮）加 pteron（翅），指短短的、像皮革的前翅。",
   "{{t:dermaptera}} comes from the Greek derma (skin) and pteron (wing), after the short leathery forewings.",
   "{{t:dermaptera}} berasal daripada bahasa Yunani derma (kulit) dan pteron (sayap), merujuk sayap depan yang pendek seperti kulit."),
 ["LSJ"],
 [Y("身体扁长，腹末有一对钳子（尾铗）", "Long flat body with a pair of pincers (forceps) at the tail", "Badan panjang leper dengan sepasang penyepit di ekor"),
  Y("前翅短而硬，膜质的后翅折在下面", "Short hard forewings with membranous hind wings folded beneath", "Sayap depan pendek keras dengan sayap belakang bermembran dilipat di bawah"),
  Y("触角细长、多节；大颚明显", "Slender many-segmented antennae; strong jaws", "Sesungut halus berbilang ruas; rahang yang kuat")],
 ["WTK:7", "TJ:33"], PART, CHEW, ["TJ:35", "WTK:7"],
 [Y("各种蠼螋，雄虫的尾铗通常比较弯", "Earwigs of several kinds; males usually have more curved forceps", "Pelbagai cocopet; jantan biasanya mempunyai penyepit yang lebih melengkung")], ["WTK:7"],
 Y("「皮」：短短的皮翅，加一把尾钳。", "Think 'skin': short leathery wings and tail pincers.", "Ingat 'kulit': sayap kulit pendek dan penyepit ekor."),
 [MC(T("蠼螋最明显的特征是？", "An earwig's most obvious feature?", "Ciri cocopet yang paling jelas?"), [T("腹末的钳子", "Pincers at the tail", "Penyepit di ekor"), T("很长的产卵器", "A long ovipositor", "Ovipositor panjang"), T("翅上的鳞片", "Scaly wings", "Sayap bersisik")], 0,
     T("蠼螋腹末有尾铗。", "Earwigs have tail forceps.", "Cocopet mempunyai penyepit ekor."), ["WTK:7", "TJ:33"]),
  TF(T("隐翅虫也有尾铗。", "Rove beetles also have tail pincers.", "Kumbang rove juga mempunyai penyepit ekor."), False,
     T("隐翅虫的翅鞘也很短，但没有尾铗。", "Rove beetles have very short wing covers but no pincers.", "Kumbang rove mempunyai penutup sayap pendek tetapi tiada penyepit."), ["TJ:172", "TJ:40"]),
  MC(T("Dermaptera 的 derma 是什么意思？", "What does 'derma' mean?", "Apakah maksud 'derma'?"), [T("皮", "Skin", "Kulit"), T("钳子", "Pincers", "Penyepit"), T("尾巴", "Tail", "Ekor")], 0,
     T("derma 是皮。", "Derma means skin.", "Derma bermaksud kulit."), ["LSJ"])])

# ---------------------------------------------------------------- p22 Neuroptera
page(22, "neuroptera", T("脉翅目（草蛉、蚁蛉）", "Neuroptera (lacewings and antlions)", "Neuroptera (lacewing dan undur-undur)"),
 T("草蛉和蚁蛉：翅透明，翅脉多如网。", "Lacewings and antlions: clear wings with net-like veins.", "Lacewing dan undur-undur: sayap jernih dengan urat seperti jaring."),
 Y("{{t:neuroptera}}来自希腊文 neuron（筋、脉）加 pteron（翅），指翅上密密麻麻像网一样的翅脉。",
   "{{t:neuroptera}} comes from the Greek neuron (sinew, vein) and pteron (wing), after the dense net of wing veins.",
   "{{t:neuroptera}} berasal daripada bahasa Yunani neuron (urat) dan pteron (sayap), merujuk jaringan urat sayap yang padat."),
 ["LSJ"],
 [Y("两对透明的翅，翅脉多如网", "Two pairs of clear wings with net-like veins", "Dua pasang sayap jernih dengan urat seperti jaring"),
  Y("身体柔软，最长约 50 毫米", "Soft body, up to about 50 mm long", "Badan lembut, sehingga kira-kira 50 mm panjang"),
  Y("触角丝状或末端膨大", "Antennae thread-like or clubbed", "Sesungut seperti benang atau berbonjol")],
 ["WTK:11"], FULL, T("咀嚼式（幼虫有吸食用的大颚）", "Chewing (larvae have sucking jaws)", "Mengunyah (larva mempunyai rahang penghisap)"), ["TJ:35", "UMN-ORD"],
 [Y("草蛉", "Green lacewings", "Lacewing hijau"),
  Y("蚁蛉：幼虫在沙地挖漏斗形陷阱，捕捉路过的小昆虫", "Antlions: larvae dig funnel traps in sand to catch passing insects", "Undur-undur: larva menggali perangkap corong dalam pasir untuk menangkap serangga yang lalu"),
  Y("长角蛉", "Owlflies", "Owlfly")], ["WTK:11", "TJ:229", "TJ:225"],
 Y("「脉」就是翅脉：翅像一张透明的网。", "Think 'veins': each wing is a clear net.", "Ingat 'urat': setiap sayap seperti jaring jernih."),
 [MC(T("蚁蛉的幼虫怎样捕食？", "How do antlion larvae catch prey?", "Bagaimana larva undur-undur menangkap mangsa?"), [T("在沙里挖陷阱", "By digging pits in sand", "Menggali perangkap dalam pasir"), T("织网", "By spinning webs", "Membuat sarang"), T("在水中追捕", "By chasing in water", "Mengejar dalam air")], 0,
     T("幼虫在沙地造沙阱。", "The larvae dig sand pits.", "Larva menggali perangkap pasir."), ["TJ:229"]),
  TF(T("脉翅目是完全变态。", "Neuroptera have complete metamorphosis.", "Neuroptera mengalami metamorfosis lengkap."), True,
     T("脉翅目经过卵、幼虫、蛹、成虫。", "Egg, larva, pupa, adult.", "Telur, larva, pupa, dewasa."), ["TJ:35"]),
  MC(T("草蛉的翅是什么样子？", "What are lacewing wings like?", "Bagaimanakah sayap lacewing?"), [T("透明，翅脉如网", "Clear, with net-like veins", "Jernih, dengan urat seperti jaring"), T("盖满鳞片", "Covered in scales", "Diliputi sisik"), T("硬壳", "Hard shells", "Cangkerang keras")], 0,
     T("脉翅目的翅像透明的网。", "Lacewing wings look like clear nets.", "Sayap lacewing seperti jaring jernih."), ["WTK:11"])])

# ---------------------------------------------------------------- p23 Ephemeroptera
page(23, "ephemeroptera", T("蜉蝣目", "Ephemeroptera (mayflies)", "Ephemeroptera (lalat sehari)"),
 T("蜉蝣：成虫寿命很短，翅竖立，尾端有长尾丝。", "Mayflies: short-lived adults with upright wings and long tails.", "Lalat sehari: dewasa berumur pendek dengan sayap tegak dan ekor panjang."),
 Y("{{t:ephemeroptera}}来自希腊文 ephemeros（只活一天）加 pteron（翅）：成虫的寿命很短。",
   "{{t:ephemeroptera}} comes from the Greek ephemeros (lasting a day) and pteron (wing): adult mayflies live only briefly.",
   "{{t:ephemeroptera}} berasal daripada bahasa Yunani ephemeros (bertahan sehari) dan pteron (sayap): lalat sehari dewasa hidup sekejap sahaja."),
 ["LSJ"],
 [Y("身体柔软，翅竖立合在背上", "Soft body; wings held upright together over the back", "Badan lembut; sayap ditegakkan bersama di atas belakang"),
  Y("后翅很小或没有", "Hind wings small or absent", "Sayap belakang kecil atau tiada"),
  Y("尾端通常有 3 条长尾丝，少数 2 条", "Usually 3 long tails, a few kinds 2", "Biasanya 3 ekor panjang, sesetengah 2"),
  Y("稚虫在水中，腹部两侧有叶片状的鳃", "Nymphs live in water with leaf-like gills along the abdomen", "Nimfa hidup dalam air dengan insang seperti daun di sepanjang abdomen")],
 ["AM-MAYFLY", "WTK:7", "WTK:9"], PART, T("成虫口器退化，不进食", "Adults have reduced mouthparts and do not feed", "Dewasa mempunyai bahagian mulut yang tidak berfungsi dan tidak makan"), ["TJ:35", "UMN-ORD"],
 [Y("溪流和池塘附近的各种蜉蝣", "Mayflies near streams and ponds", "Lalat sehari berhampiran sungai dan kolam")], ["WTK:7"],
 Y("「蜉蝣」：成虫一生很短，所以叫「朝生暮死」。", "Think 'ephemeral': the adult's life is very short.", "Ingat 'sementara': hayat dewasa sangat singkat."),
 [MC(T("蜉蝣成虫的翅怎样摆？", "How do adult mayflies hold their wings?", "Bagaimana lalat sehari dewasa meletakkan sayapnya?"), [T("竖立在背上", "Upright over the back", "Tegak di atas belakang"), T("平贴腹部", "Flat over the abdomen", "Rata di atas abdomen"), T("向两侧平展", "Spread out flat", "Terbentang rata")], 0,
     T("蜉蝣的翅竖立合在背上。", "Mayflies hold their wings upright.", "Lalat sehari menegakkan sayapnya."), ["AM-MAYFLY"]),
  MC(T("怎样分蜉蝣和石蝇？", "How do you tell a mayfly from a stonefly?", "Bagaimana membezakan lalat sehari dan lalat batu?"), [T("石蝇每只脚两个爪、两条尾须", "Stoneflies have two claws per foot and two tails", "Lalat batu mempunyai dua kuku setiap kaki dan dua ekor"), T("蜉蝣没有翅", "Mayflies have no wings", "Lalat sehari tiada sayap")], 0,
     T("蜉蝣每只脚一个爪，稚虫腹部有叶状鳃。", "Mayflies have one claw per foot, and nymphs have leaf-like gills.", "Lalat sehari mempunyai satu kuku setiap kaki, dan nimfanya ada insang seperti daun."), ["WTK:9"]),
  TF(T("蜉蝣的稚虫生活在水中。", "Mayfly nymphs live in water.", "Nimfa lalat sehari hidup dalam air."), True,
     T("稚虫用腹部两侧的鳃呼吸。", "They breathe with gills along the abdomen.", "Ia bernafas dengan insang di sepanjang abdomen."), ["WTK:9"])],
 compare={"heading": T("蜉蝣还是石蝇？", "Mayfly or stonefly?", "Lalat sehari atau lalat batu?"), "blocks": [
  {"type": "table", "src": ["WTK:9", "AM-MAYFLY"], "caption": T("看翅、尾和脚爪", "Look at the wings, tails and claws", "Lihat sayap, ekor dan kuku"),
   "headers": [T("比较", "Compare", "Banding"), T("蜉蝣", "Mayfly", "Lalat sehari"), T("石蝇", "Stonefly", "Lalat batu")],
   "rows": [[T("翅", "Wings", "Sayap"), T("竖立在背上", "Held upright", "Ditegakkan"), T("平贴或包着身体", "Folded flat or around the body", "Dilipat rata atau di sekeliling badan")],
            [T("尾", "Tails", "Ekor"), T("通常 3 条", "Usually 3", "Biasanya 3"), T("2 条", "2", "2")],
            [T("脚爪", "Claws", "Kuku"), T("每只脚 1 个", "1 per foot", "1 setiap kaki"), T("每只脚 2 个", "2 per foot", "2 setiap kaki")],
            [T("稚虫的鳃", "Nymph gills", "Insang nimfa"), T("腹部两侧叶状鳃", "Leaf-like gills on the abdomen", "Insang seperti daun pada abdomen"), T("腹部两侧没有这种鳃", "No such gills on the abdomen", "Tiada insang sebegitu pada abdomen")]]}]})

# ---------------------------------------------------------------- p24 Trichoptera
page(24, "trichoptera", T("毛翅目（石蛾）", "Trichoptera (caddisflies)", "Trichoptera (lalat kadis)"),
 T("石蛾：像蛾，但翅上是细毛不是鳞片。", "Caddisflies: moth-like, with hairy rather than scaly wings.", "Lalat kadis: seperti kupu-kupu, tetapi sayapnya berbulu, bukan bersisik."),
 Y("{{t:trichoptera}}来自希腊文 thrix（毛）加 pteron（翅），意思是「有毛的翅」。",
   "{{t:trichoptera}} comes from the Greek thrix (hair) and pteron (wing): 'hairy-winged'.",
   "{{t:trichoptera}} berasal daripada bahasa Yunani thrix (rambut) dan pteron (sayap): 'bersayap berbulu'."),
 ["LSJ"],
 [Y("两对多毛的膜质翅，看起来像蛾", "Two pairs of hairy membranous wings; looks like a moth", "Dua pasang sayap bermembran berbulu; kelihatan seperti kupu-kupu"),
  Y("停下时翅呈屋脊状盖在身上", "Wings held tent-like over the body at rest", "Sayap seperti khemah di atas badan ketika berehat"),
  Y("触角细长如线，常比身体长", "Long thread-like antennae, often longer than the body", "Sesungut panjang seperti benang, sering lebih panjang daripada badan")],
 ["WTK:8", "AM-MAYFLY"], FULL, CHEW, ["TJ:35", "UMN-ORD"],
 [Y("溪流附近的石蛾，常被灯光吸引", "Caddisflies near streams, often drawn to lights", "Lalat kadis berhampiran sungai, sering tertarik kepada cahaya")], ["WTK:8"],
 Y("「毛」：翅上是毛，不是鳞。", "Think 'hair': hairy wings, not scaly ones.", "Ingat 'bulu': sayap berbulu, bukan bersisik."),
 [MC(T("石蛾和蛾怎样分？", "How do you tell a caddisfly from a moth?", "Bagaimana membezakan lalat kadis dan kupu-kupu?"), [T("石蛾翅上是毛，蛾翅上是鳞", "Caddisfly wings are hairy, moth wings scaly", "Sayap lalat kadis berbulu, sayap kupu-kupu bersisik"), T("石蛾没有触角", "Caddisflies have no antennae", "Lalat kadis tiada sesungut")], 0,
     T("蛾的触角常羽状或锯齿状，石蛾的细长如线。", "Moths often have feathery or saw-edged antennae; caddisflies thread-like.", "Kupu-kupu sering bersesungut berbulu atau bergerigi; lalat kadis seperti benang."), ["WTK:8"]),
  TF(T("石蛾是完全变态。", "Caddisflies have complete metamorphosis.", "Lalat kadis mengalami metamorfosis lengkap."), True,
     T("毛翅目经过卵、幼虫、蛹、成虫。", "Egg, larva, pupa, adult.", "Telur, larva, pupa, dewasa."), ["TJ:35"]),
  MC(T("Trichoptera 的 thrix 是什么意思？", "What does 'thrix' mean?", "Apakah maksud 'thrix'?"), [T("毛", "Hair", "Rambut"), T("石头", "Stone", "Batu"), T("水", "Water", "Air")], 0,
     T("thrix 是毛。", "Thrix means hair.", "Thrix bermaksud rambut."), ["LSJ"])])

# ---------------------------------------------------------------- p25 Zygentoma
page(25, "zygentoma", T("衣鱼目", "Zygentoma (silverfish)", "Zygentoma (gegat)"),
 T("衣鱼：无翅、扁长、尾端三条长丝。", "Silverfish: wingless, flat, with three long tails.", "Gegat: tidak bersayap, leper, dengan tiga ekor panjang."),
 Y("{{t:zygentoma}}以前叫 Thysanura，来自希腊文 thysanos（缨）加 oura（尾），指尾端的三条长丝。",
   "{{t:zygentoma}} used to be called Thysanura, from the Greek thysanos (fringe) and oura (tail), after the three long tail threads.",
   "{{t:zygentoma}} dahulu dipanggil Thysanura, daripada bahasa Yunani thysanos (jumbai) dan oura (ekor), merujuk tiga ekor panjang."),
 ["LSJ", "WTK:10"],
 [Y("没有翅，身体扁长，常有银灰色鳞片", "Wingless, flat and long, often with silvery scales", "Tidak bersayap, leper dan panjang, sering bersisik keperakan"),
  Y("触角很长", "Long antennae", "Sesungut panjang"),
  Y("尾端有三条长丝", "Three long tail threads", "Tiga ekor panjang")],
 ["WTK:10"], NONE, CHEW, ["TJ:34", "UMN-ORD"],
 [Y("家中的衣鱼，会咬坏书本和纸张", "Household silverfish, which damage books and paper", "Gegat rumah, yang merosakkan buku dan kertas")], ["WTK:10"],
 Y("「衣鱼」：银色的小鱼，在书堆里游。", "Think 'silver fish': a little silver swimmer in your books.", "Ingat 'ikan perak': perenang perak kecil di celah buku."),
 [MC(T("衣鱼的尾端有几条长丝？", "How many tail threads does a silverfish have?", "Berapa ekor panjang gegat?"), [T("3 条", "3", "3"), T("1 条", "1", "1"), T("没有", "None", "Tiada")], 0,
     T("衣鱼尾端有三条长丝。", "Silverfish have three tail threads.", "Gegat mempunyai tiga ekor."), ["WTK:10"]),
  TF(T("衣鱼长大后还会继续蜕皮。", "Silverfish keep moulting after they are adult.", "Gegat terus bersalin kulit selepas dewasa."), True,
     T("无变态的昆虫性成熟后仍会蜕皮。", "Ametabolous insects moult even after maturing.", "Serangga ametabola bersalin kulit walaupun selepas matang."), ["TJ:34"]),
  MC(T("衣鱼在家里会损坏什么？", "What do silverfish damage at home?", "Apakah yang dirosakkan gegat di rumah?"), [T("书本和纸张", "Books and paper", "Buku dan kertas"), T("电线", "Wires", "Wayar"), T("玻璃", "Glass", "Kaca")], 0,
     T("衣鱼会咬坏书本。", "Silverfish damage books.", "Gegat merosakkan buku."), ["WTK:10"])])

# ---------------------------------------------------------------- p26 Lesser orders
page(26, "lesser-orders", T("其他较少见的目", "Less common orders", "Order yang kurang biasa"),
 T("襀翅目、广翅目、长翅目、蚤目、虱目、纺足目、缺翅目。", "Stoneflies, alderflies and fishflies, scorpionflies, fleas, lice, webspinners and angel insects.", "Lalat batu, alderfly dan fishfly, lalat kala jengking, kutu, tuma, labah-labah sutera dan serangga malaikat."),
 Y("除了常见的目，马来西亚还有一些不常碰到的目。下面列出每一目最容易认的特征；{{t:lesser-orders}}的成员大多很小，或住在水边、土里、动物身上。",
   "Besides the common orders, Malaysia has some you will meet less often. Below are the easiest features of each; members of these {{t:lesser-orders}} are mostly small, or live by water, in soil or on animals.",
   "Selain order biasa, Malaysia juga mempunyai beberapa order yang jarang ditemui. Berikut ialah ciri paling mudah setiap satu; ahli {{t:lesser-orders}} kebanyakannya kecil, atau hidup di tepi air, dalam tanah atau pada haiwan."),
 ["WTK:8-11"],
 [Y("襀翅目（石蝇）：两条尾须，身体扁长柔软，每只脚两个爪", "Plecoptera (stoneflies): two tails, long flat soft body, two claws on each foot", "Plecoptera (lalat batu): dua ekor, badan panjang leper lembut, dua kuku setiap kaki"),
  Y("广翅目（泥蛉、鱼蛉）：大型，翅脉多；鱼蛉停下时翅平贴身体", "Megaloptera (alderflies, fishflies): large with many wing veins; fishflies rest with wings folded flat", "Megaloptera (alderfly, fishfly): besar dengan banyak urat sayap; fishfly berehat dengan sayap dilipat rata"),
  Y("长翅目（蝎蛉）：头伸长成喙，雄虫腹末像蝎子一样向上弯", "Mecoptera (scorpionflies): head drawn out into a beak; the male's tail curls up like a scorpion's", "Mecoptera (lalat kala jengking): kepala memanjang seperti paruh; ekor jantan melengkung seperti kala jengking"),
  Y("蚤目（跳蚤）：身体左右扁平，后足善跳，触角很短", "Siphonaptera (fleas): flattened from side to side, jumping hind legs, very short antennae", "Siphonaptera (kutu): leper dari sisi ke sisi, kaki belakang pelompat, sesungut sangat pendek"),
  Y("虱目（虱子）：通常不到 10 毫米，触角短而粗", "Phthiraptera (lice): usually under 10 mm, short stubby antennae", "Phthiraptera (tuma): biasanya kurang 10 mm, sesungut pendek dan tebal"),
  Y("纺足目（足丝蚁）：4–15 毫米，前足跗节膨大、能吐丝筑隧道，雌虫无翅", "Embioptera (webspinners): 4–15 mm, swollen front feet that spin silk tunnels, wingless females", "Embioptera (labah-labah sutera): 4–15 mm, tapak kaki depan membengkak yang memintal terowong sutera, betina tidak bersayap"),
  Y("缺翅目（缺翅虫）：小而柔软，触角念珠状，住在腐木里", "Zoraptera (angel insects): small and soft, bead-like antennae, live in rotting wood", "Zoraptera (serangga malaikat): kecil dan lembut, sesungut seperti manik, hidup dalam kayu reput")],
 ["WTK:8", "WTK:9", "WTK:10", "WTK:11", "MDC-FISH"],
 T("石蝇、跳蚤、虱子、足丝蚁、缺翅虫等各不相同", "Varies: see each order", "Berbeza mengikut order"),
 T("各不相同", "Varies", "Berbeza"), ["TJ:35"],
 [Y("鱼蛉以前常被误放在蜉蝣目，其实属于广翅目", "Fishflies are sometimes listed with mayflies, but they belong to Megaloptera", "Fishfly kadang-kadang disenaraikan bersama lalat sehari, tetapi ia tergolong dalam Megaloptera"),
  Y("蜱有八只脚，是蛛形纲动物，不是跳蚤的亲戚", "Ticks have eight legs and are arachnids, not relatives of fleas", "Sengkenit berkaki lapan dan ialah araknid, bukan saudara kutu")], ["MDC-FISH", "WTK:10"],
 Y("先数尾巴、看脚爪：两条尾、两个爪是石蝇。", "Count tails and claws: two tails and two claws make a stonefly.", "Kira ekor dan kuku: dua ekor dan dua kuku ialah lalat batu."),
 [MC(T("鱼蛉属于哪一目？", "Which order do fishflies belong to?", "Fishfly tergolong dalam order mana?"), [T("广翅目", "Megaloptera", "Megaloptera"), T("蜉蝣目", "Ephemeroptera", "Ephemeroptera"), T("双翅目", "Diptera", "Diptera")], 0,
     T("鱼蛉和齿蛉都属于广翅目。", "Fishflies and dobsonflies are Megaloptera.", "Fishfly dan dobsonfly ialah Megaloptera."), ["MDC-FISH"]),
  MC(T("跳蚤的身体是怎样扁的？", "How is a flea's body flattened?", "Bagaimanakah badan kutu leper?"), [T("左右扁平", "From side to side", "Dari sisi ke sisi"), T("上下扁平", "From top to bottom", "Dari atas ke bawah")], 0,
     T("跳蚤身体左右扁平，便于在毛发间穿行。", "Fleas are flattened sideways.", "Kutu leper dari sisi ke sisi."), ["WTK:10"]),
  TF(T("纺足目的雌虫没有翅。", "Female webspinners are wingless.", "Labah-labah sutera betina tidak bersayap."), True,
     T("纺足目雌虫无翅，前足能吐丝。", "Females are wingless; the front feet spin silk.", "Betina tidak bersayap; tapak kaki depan memintal sutera."), ["WTK:11"])])
