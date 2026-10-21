"""The identification key (data/key.json).

Taijiang guide pp. 38-40 (TJ), extended for Malaysia with stick insects,
mayflies, caddisflies, thrips and silverfish (WTK, UMD-THRIPS). Adults only.
Every question also offers "none of these", which ends at `outside`."""
import json
import sys
sys.path.insert(0, 'tools/content')
from build import T, T2

NONE = T("以上都不是／看不出来", "None of these / can't tell", "Tiada yang sesuai / tidak pasti")


def O(label, next=None, result=None):
    o = {"label": label}
    if next:
        o["next"] = next
    if result:
        o["result"] = result
    return o


def N(q, hint, *options, img=None):
    n = {"q": q, "hint": hint, "options": [*options, O(NONE, result="outside")]}
    if img:
        n["img"] = img
    return n


nodes = {
 "shape": N(T("它的身体是不是细长得像一根树枝，或扁平得像一片叶子？", "Does its body look like a twig, or flat like a leaf?", "Adakah badannya kelihatan seperti ranting, atau leper seperti daun?"),
   T("竹节虫和叶䗛靠伪装：身体、脚甚至翅都像植物，静止不动时很难发现。", "Stick and leaf insects hide by looking like plants: body, legs and even wings copy twigs or leaves, and they keep still.", "Serangga ranting dan serangga daun bersembunyi dengan menyerupai tumbuhan, dan mereka tidak bergerak."),
   O(T("像树枝或叶子", "Yes, like a twig or a leaf", "Ya, seperti ranting atau daun"), result="phasmids"),
   O(T("不像", "No", "Tidak"), next="wings"), img="img/svg/key-shape.svg"),
 "wings": N(T("有没有翅？", "Does it have wings?", "Adakah ia bersayap?"),
   T("翅可能折叠在背上，或藏在硬壳下面。从侧面或背面看清楚；有硬壳也算有翅。", "Wings may be folded flat on the back or hidden under hard covers; hard wing covers count as wings.", "Sayap mungkin terlipat di belakang atau tersembunyi di bawah penutup keras; penutup sayap keras dikira sebagai sayap."),
   O(T("有翅（包括硬壳状的翅）", "Yes (hard wing covers count)", "Ya (penutup sayap keras dikira)"), next="pairs"),
   O(T("没有翅", "No wings", "Tiada sayap"), next="wingless-where"), img="img/svg/key-wings.svg"),
 "wingless-where": N(T("它生活在哪里？", "Where is it living?", "Di manakah ia hidup?"),
   T("在水面上滑行的无翅昆虫多半是黾蝽（水黾、海黾）。", "Wingless insects skating on the water surface are usually water striders.", "Serangga tanpa sayap yang meluncur di permukaan air biasanya pepijat air (water strider)."),
   O(T("在水面上滑行", "Skating on the water surface", "Meluncur di permukaan air"), result="water-striders"),
   O(T("在陆地上", "On land", "Di darat"), next="wingless-land")),
 "wingless-land": N(T("它的触角和身体是什么样子？", "What do its antennae and body look like?", "Bagaimanakah rupa sesungut dan badannya?"),
   T("念珠状触角像一串小珠子；膝状触角在中间折成一个角，像手肘。", "Bead-like antennae look like a string of small beads; elbowed antennae bend sharply in the middle.", "Sesungut seperti manik kelihatan seperti rantai manik kecil; sesungut bersiku bengkok tajam di tengah."),
   O(T("触角像一串珠子，身体软、颜色淡", "Bead-like antennae, soft pale body", "Sesungut seperti manik, badan lembut dan pucat"), result="termites-workers"),
   O(T("触角在中间折成膝状，腰很细", "Elbowed antennae and a narrow waist", "Sesungut bersiku dan pinggang sempit"), result="ants-workers"),
   O(T("身体扁长、有银色鳞片，尾端有三条长丝", "Flat, silvery-scaled body with three long tail threads", "Badan leper bersisik perak dengan tiga ekor panjang"), result="silverfish"), img="img/svg/key-antennae.svg"),
 "pairs": N(T("有几对翅？", "How many pairs of wings?", "Berapa pasang sayap?"),
   T("双翅目只有一对翅，后翅变成一对小棒（平衡棒）。蜉蝣的后翅很小或看不见，但腹末有 2–3 条长尾丝。", "Flies have one pair; their hind wings are tiny knobs (halteres). Mayflies' hind wings are tiny or absent, but they have 2–3 long tail threads.", "Lalat mempunyai sepasang sayap; sayap belakangnya menjadi tombol kecil (halter). Sayap belakang lalat sehari sangat kecil atau tiada, tetapi ia mempunyai 2–3 ekor panjang."),
   O(T("一对翅（后面有一对小棒）", "One pair (with tiny knobs behind)", "Sepasang (dengan tombol kecil di belakang)"), next="fly-antennae"),
   O(T("两对翅", "Two pairs", "Dua pasang"), next="scales"),
   O(T("翅竖立在背上，后翅很小或看不见，腹末有 2–3 条长尾丝", "Wings held upright, hind wings tiny or absent, 2–3 long tail threads", "Sayap tegak, sayap belakang kecil atau tiada, 2–3 ekor panjang"), result="mayflies"), img="img/svg/key-pairs.svg"),
 "fly-antennae": N(T("触角是长还是短？", "Are the antennae long or short?", "Adakah sesungutnya panjang atau pendek?"),
   T("家蝇、实蝇的触角很短，藏在脸前；蚊、蠓的触角细长、有很多节，雄蚊的触角像羽毛。", "House flies and fruit flies have very short antennae; mosquitoes and midges have long, many-segmented antennae (feathery in males).", "Lalat rumah dan lalat buah mempunyai sesungut sangat pendek; nyamuk dan agas mempunyai sesungut panjang berbilang ruas."),
   O(T("短", "Short", "Pendek"), result="flies"),
   O(T("长，有很多节", "Long, with many segments", "Panjang, berbilang ruas"), result="mosquitoes")),
 "scales": N(T("翅上有没有鳞粉？", "Are the wings covered in scales?", "Adakah sayapnya diliputi sisik?"),
   T("蝶和蛾的翅上盖满细小的鳞片，摸到会留下彩色粉末。不要用手去摸活的昆虫，从近处看翅面是否像粉末。", "Butterfly and moth wings are covered in tiny scales that rub off as coloured dust. Look closely rather than touching.", "Sayap rama-rama dan kupu-kupu diliputi sisik halus yang tertanggal seperti debu berwarna. Lihat dekat-dekat dan jangan sentuh."),
   O(T("有鳞粉", "Yes, scaly", "Ya, bersisik"), result="butterflies-moths"),
   O(T("没有鳞粉", "No scales", "Tiada sisik"), next="thrips"), img="img/svg/key-scales.svg"),
 "thrips": N(T("它是不是非常小（1–2 毫米），翅很窄、边缘有长毛，像羽毛？", "Is it tiny (1–2 mm) with narrow wings fringed with long hairs, like feathers?", "Adakah ia sangat kecil (1–2 mm) dengan sayap sempit berjumbai bulu panjang?"),
   T("蓟马细长像米粒，常在花里或嫩叶上。需要放大镜才看得清翅边的长毛。", "Thrips are slender like a grain of rice and live in flowers and young leaves; you need a hand lens to see the fringe.", "Trips langsing seperti sebutir beras dan hidup dalam bunga dan daun muda; perlukan kanta pembesar untuk melihat jumbai."),
   O(T("是", "Yes", "Ya"), result="thrips"),
   O(T("不是", "No", "Tidak"), next="mouth")),
 "mouth": N(T("口器是不是像一根针管，平时收在头下？", "Is the mouth a needle-like beak folded under the head?", "Adakah mulutnya seperti paruh jarum yang dilipat di bawah kepala?"),
   T("刺吸式口器用来刺进植物或动物吸食汁液。从侧面看，头下有一根伸向后方的细管。", "A piercing-sucking beak is used to pierce plants or animals and suck fluids; from the side it shows as a thin tube under the head.", "Mulut penusuk-penghisap digunakan untuk menusuk tumbuhan atau haiwan dan menghisap cecair."),
   O(T("是，针管状口器", "Yes, a needle-like beak", "Ya, paruh seperti jarum"), next="bug-wings"),
   O(T("不是", "No", "Tidak"), next="texture"), img="img/svg/key-mouth.svg"),
 "bug-wings": N(T("前翅是什么样子？", "What are the forewings like?", "Bagaimanakah sayap depannya?"),
   T("蝽的前翅前半段硬、后半段薄而透明（半鞘翅），停栖时在背上交叠。蝉、叶蝉、蚜虫的翅全部是膜质，停栖时像屋顶。", "True bugs have forewings hard at the base and thin at the tip, overlapping on the back. Cicadas, hoppers and aphids have wholly membranous wings held like a roof.", "Pepijat sebenar mempunyai sayap depan keras di pangkal dan nipis di hujung. Riang-riang, bena dan afid mempunyai sayap bermembran sepenuhnya."),
   O(T("前半段硬、后半段膜质", "Hard at the base, thin at the tip", "Keras di pangkal, nipis di hujung"), result="true-bugs"),
   O(T("全部是膜质", "Thin and membranous all over", "Nipis bermembran sepenuhnya"), result="cicadas-hoppers")),
 "texture": N(T("前翅和后翅的质地一样吗？", "Are the forewings and hind wings the same texture?", "Adakah sayap depan dan belakang sama teksturnya?"),
   T("甲虫的前翅是硬壳，螽斯的前翅像皮革；蜂、蜻蜓的前后翅都是透明的薄膜。", "A beetle's forewings are hard shells and a katydid's are leathery; bees and dragonflies have clear membranes front and back.", "Sayap depan kumbang ialah cangkerang keras dan sayap depan katidid seperti kulit; lebah dan pepatung mempunyai membran jernih di depan dan belakang."),
   O(T("一样（都是薄膜）", "Same (all membranous)", "Sama (semuanya membran)"), next="rest"),
   O(T("不一样（前翅较硬或像皮革）", "Different (forewings hard or leathery)", "Berbeza (sayap depan keras atau seperti kulit)"), next="forceps")),
 "rest": N(T("停下来时，翅怎么摆？", "How does it hold its wings at rest?", "Bagaimanakah ia meletakkan sayap ketika berehat?"),
   T("蜻蜓、豆娘停下时翅竖起或平展；蜂、白蚁、草蛉把翅平贴或像屋顶一样盖在背上。", "Dragonflies and damselflies hold wings out flat or upright; bees, termites and lacewings fold them over the back.", "Pepatung dan pepatung jarum mengangkat atau mendatarkan sayap; lebah, anai-anai dan lacewing melipatnya di atas belakang."),
   O(T("平贴背上，或像屋顶盖着身体", "Folded flat or roof-like over the body", "Dilipat rata atau seperti bumbung"), next="waist"),
   O(T("竖立，或向两侧平展", "Held upright or spread out flat", "Tegak atau terbentang rata"), next="odo-antennae")),
 "waist": N(T("胸和腹之间有没有很细的腰？", "Is there a narrow waist between thorax and abdomen?", "Adakah pinggang sempit antara toraks dan abdomen?"),
   T("蜂和蚂蚁的腹部基部收窄，像有一条腰带。", "In bees, wasps and ants the abdomen narrows sharply at its base.", "Pada lebah, tebuan dan semut, abdomen menyempit dengan ketara di pangkalnya."),
   O(T("没有明显的腰", "No obvious waist", "Tiada pinggang yang jelas"), next="no-waist"),
   O(T("有明显的腰", "A clear narrow waist", "Pinggang sempit yang jelas"), next="node"), img="img/svg/key-waist.svg"),
 "no-waist": N(T("哪一项最像？", "Which fits best?", "Yang manakah paling sesuai?"),
   T("有翅白蚁常在下雨前后的傍晚成群飞向灯光，翅很容易脱落。石蛾像蛾，但翅上是细毛不是鳞片。", "Winged termites swarm to lights around rain and shed their wings easily. Caddisflies look like moths but their wings carry hairs, not scales.", "Anai-anai bersayap berkerumun ke lampu ketika hujan dan mudah menanggalkan sayap. Lalat kadis seperti kupu-kupu tetapi sayapnya berbulu, bukan bersisik."),
   O(T("触角像一串珠子，四片翅几乎一样大", "Bead-like antennae; four nearly equal wings", "Sesungut seperti manik; empat sayap hampir sama besar"), result="termites-alates"),
   O(T("翅上有细毛，停下时呈屋脊状，触角细长如线", "Hairy wings held roof-like; long thread-like antennae", "Sayap berbulu seperti bumbung; sesungut panjang seperti benang"), result="caddisflies"),
   O(T("翅透明、翅脉多如网", "Clear wings with a dense net of veins", "Sayap jernih dengan urat seperti jaring"), result="lacewings")),
 "node": N(T("腰上有没有一两个结状突起？", "Does the waist have one or two bumps (nodes)?", "Adakah pinggangnya mempunyai satu atau dua bonjol (nod)?"),
   T("有翅的蚂蚁（繁殖蚁）腰上有一或两个小结，触角膝状。蜂类的腰是平滑的。", "Winged ants have one or two nodes on the waist and elbowed antennae; bees and wasps have a smooth waist.", "Semut bersayap mempunyai satu atau dua nod pada pinggang dan sesungut bersiku; lebah dan tebuan mempunyai pinggang licin."),
   O(T("有结状突起", "Yes, with nodes", "Ya, ada nod"), result="ants-alates"),
   O(T("没有", "No, smooth", "Tidak, licin"), result="bees-wasps")),
 "odo-antennae": N(T("触角是短还是长？", "Are the antennae short or long?", "Adakah sesungutnya pendek atau panjang?"),
   T("蜻蜓、豆娘的触角短得几乎看不见；长角蛉的触角很长，末端膨大。", "Dragonflies and damselflies have tiny bristle-like antennae; owlflies have long antennae with a knob at the tip.", "Pepatung mempunyai sesungut sangat pendek; owlfly mempunyai sesungut panjang dengan tombol di hujung."),
   O(T("很短，几乎看不见", "Very short, barely visible", "Sangat pendek, hampir tidak kelihatan"), next="odo-wings"),
   O(T("很长，末端膨大", "Long, knobbed at the tip", "Panjang, berbonjol di hujung"), result="owlflies")),
 "odo-wings": N(T("前翅和后翅一样大吗？", "Are the fore- and hind wings the same size?", "Adakah sayap depan dan belakang sama besar?"),
   T("豆娘四片翅形状差不多，停下时多半合起在背上，两眼分开。蜻蜓的后翅基部较宽，停下时翅平展，两眼常相接。", "Damselflies have four similar wings, usually closed over the back, and widely separated eyes. Dragonflies have broader hind wings held flat, and eyes that often meet.", "Pepatung jarum mempunyai empat sayap yang serupa dan mata yang berjauhan. Pepatung mempunyai sayap belakang lebih lebar yang terbentang dan mata yang sering bertemu."),
   O(T("差不多大，停下时多合起", "About equal, usually closed at rest", "Hampir sama, biasanya tertutup ketika berehat"), result="damselflies"),
   O(T("后翅较宽，停下时平展", "Hind wings broader, held flat at rest", "Sayap belakang lebih lebar, terbentang ketika berehat"), result="dragonflies")),
 "forceps": N(T("腹部末端有没有一对钳子（尾铗）？", "Is there a pair of pincers at the tip of the abdomen?", "Adakah sepasang penyepit di hujung abdomen?"),
   T("蠼螋腹末的尾铗很明显，前翅短小。", "Earwigs carry obvious pincers and have short forewings.", "Cocopet (earwig) mempunyai penyepit yang jelas dan sayap depan pendek."),
   O(T("有", "Yes", "Ya"), result="earwigs"),
   O(T("没有", "No", "Tidak"), next="elytra"), img="img/svg/key-forceps.svg"),
 "elytra": N(T("前翅是不是硬壳，在背中央合成一条直线？", "Are the forewings hard shells meeting in a straight line down the back?", "Adakah sayap depannya cangkerang keras yang bertemu dalam garis lurus di belakang?"),
   T("甲虫的前翅叫翅鞘，盖住后翅和腹部，两片在背中线对齐。", "A beetle's forewings (elytra) cover the hind wings and abdomen and meet in a straight line down the middle.", "Sayap depan kumbang (elitra) menutupi sayap belakang dan abdomen serta bertemu dalam garis lurus di tengah."),
   O(T("是", "Yes", "Ya"), result="beetles"),
   O(T("不是", "No", "Tidak"), next="raptorial"), img="img/svg/key-elytra.svg"),
 "raptorial": N(T("前脚是不是像镰刀，用来抓猎物？", "Are the front legs like folding blades for grabbing prey?", "Adakah kaki depannya seperti pisau lipat untuk menangkap mangsa?"),
   T("螳螂的前足有刺，可以折起来夹住猎物。", "A mantis's front legs are spiny and fold shut on prey.", "Kaki depan cengkadak berduri dan dilipat untuk menangkap mangsa."),
   O(T("是", "Yes", "Ya"), result="mantids"),
   O(T("不是", "No", "Tidak"), next="hindlegs"), img="img/svg/key-raptorial.svg"),
 "hindlegs": N(T("后脚是不是特别粗大，用来跳？", "Are the hind legs much thicker, made for jumping?", "Adakah kaki belakangnya jauh lebih tebal, untuk melompat?"),
   T("蝗虫、螽斯、蟋蟀的后腿粗壮。", "Grasshoppers, katydids and crickets have stout hind legs.", "Belalang, katidid dan cengkerik mempunyai kaki belakang yang tegap."),
   O(T("是", "Yes", "Ya"), next="ortho-antennae"),
   O(T("不是", "No", "Tidak"), next="digging"), img="img/svg/key-hindlegs.svg"),
 "ortho-antennae": N(T("触角比身体长，还是短？", "Are the antennae longer or shorter than the body?", "Adakah sesungutnya lebih panjang atau lebih pendek daripada badan?"),
   T("螽斯、蟋蟀的触角细长，常比身体还长；蝗虫的触角短而粗。", "Katydids and crickets have hair-thin antennae, often longer than the body; grasshoppers have short, thick ones.", "Katidid dan cengkerik mempunyai sesungut halus yang sering lebih panjang daripada badan; belalang mempunyai sesungut pendek dan tebal."),
   O(T("很长", "Long", "Panjang"), result="katydids-crickets"),
   O(T("短", "Short", "Pendek"), result="grasshoppers")),
 "digging": N(T("前脚是不是又宽又扁，像铲子？", "Are the front legs broad and flat like spades?", "Adakah kaki depannya lebar dan leper seperti penyodok?"),
   T("蝼蛄用铲状前足在土里挖洞。", "Mole crickets dig through soil with spade-like front legs.", "Anjing tanah (cengkerik tanah) menggali tanah dengan kaki depan seperti penyodok."),
   O(T("是", "Yes", "Ya"), result="mole-crickets"),
   O(T("不是", "No", "Tidak"), result="cockroaches")),
}

TJ = ["TJ:38-40"]


def R(group, order, check, confused, src=TJ):
    return {"group": group, "order": order, "check": check, "confused": confused, "src": src}


results = {
 "outside": {"group": T("不在本检索表内", "Not covered by this key", "Tiada dalam kunci ini"), "order": None,
   "check": [T("不在本检索表内，请请教专家", "Not covered by this key — ask an expert", "Tiada dalam kunci ini — rujuk pakar")], "confused": [], "src": TJ},
 "phasmids": R(T("竹节虫、叶䗛", "Stick and leaf insects", "Serangga ranting dan serangga daun"), "p19",
   [T("身体像树枝或叶子", "Body like a twig or leaf", "Badan seperti ranting atau daun"), T("脚细长，行动缓慢", "Long thin legs, slow movements", "Kaki panjang halus, bergerak perlahan")],
   [T("螳螂（前足为捕捉足）", "Mantids (grasping front legs)", "Cengkadak (kaki depan penangkap)")], ["WTK:6"]),
 "water-striders": R(T("黾蝽（水黾、海黾）", "Water striders", "Pepijat air (water strider)"), "p12",
   [T("在水面上滑行", "Skates on the water surface", "Meluncur di permukaan air"), T("中、后足很长", "Long middle and hind legs", "Kaki tengah dan belakang panjang")], [], ["TJ:38", "WTK:1"]),
 "termites-workers": R(T("白蚁（工蚁）", "Termites (workers)", "Anai-anai (pekerja)"), "p18",
   [T("触角念珠状", "Bead-like antennae", "Sesungut seperti manik"), T("身体软、颜色淡，没有细腰", "Soft pale body, no narrow waist", "Badan lembut pucat, tiada pinggang sempit")],
   [T("蚂蚁：触角膝状、有细腰", "Ants: elbowed antennae and a narrow waist", "Semut: sesungut bersiku dan pinggang sempit")], ["TJ:38", "WTK:4"]),
 "ants-workers": R(T("蚂蚁（工蚁）", "Ants (workers)", "Semut (pekerja)"), "p13",
   [T("触角膝状", "Elbowed antennae", "Sesungut bersiku"), T("腰细，腰上有结", "Narrow waist with a node", "Pinggang sempit dengan nod")],
   [T("白蚁：触角念珠状、没有细腰", "Termites: bead-like antennae, no waist", "Anai-anai: sesungut seperti manik, tiada pinggang")]),
 "silverfish": R(T("衣鱼", "Silverfish", "Gegat"), "p25",
   [T("身体扁长，有银灰色鳞片", "Flat body with silvery scales", "Badan leper dengan sisik keperakan"), T("尾端有三条长丝", "Three long tail threads", "Tiga ekor panjang")],
   [], ["WTK:10"]),
 "mayflies": R(T("蜉蝣", "Mayflies", "Lalat sehari (mayfly)"), "p23",
   [T("翅竖立在背上", "Wings held upright over the back", "Sayap tegak di atas belakang"), T("腹末有 2–3 条长尾丝", "2–3 long tail threads", "2–3 ekor panjang")],
   [T("石蝇：只有 2 条尾须，翅平贴腹部", "Stoneflies: 2 tails, wings folded flat", "Lalat batu: 2 ekor, sayap dilipat rata")], ["WTK:7", "WTK:9"]),
 "flies": R(T("蝇、虻", "Flies", "Lalat"), "p14",
   [T("只有一对翅", "One pair of wings", "Sepasang sayap"), T("触角很短", "Very short antennae", "Sesungut sangat pendek")],
   [T("食蚜蝇像蜜蜂，但只有一对翅", "Hoverflies look like bees but have one pair of wings", "Lalat bunga seperti lebah tetapi bersayap sepasang")], ["TJ:38", "WTK:6"]),
 "mosquitoes": R(T("蚊、蠓、蚋", "Mosquitoes and midges", "Nyamuk dan agas"), "p14",
   [T("只有一对翅", "One pair of wings", "Sepasang sayap"), T("触角细长、多节", "Long, many-segmented antennae", "Sesungut panjang berbilang ruas")], [], ["TJ:38", "WTK:6"]),
 "butterflies-moths": R(T("蝶、蛾", "Butterflies and moths", "Rama-rama dan kupu-kupu"), "p11",
   [T("翅上有鳞粉", "Wings covered in scales", "Sayap diliputi sisik"), T("口器是卷起的长吸管", "Coiled sucking tube for a mouth", "Mulut berupa tiub penghisap bergulung")],
   [T("石蛾：翅上是细毛，不是鳞片", "Caddisflies: hairy, not scaly, wings", "Lalat kadis: sayap berbulu, bukan bersisik")], ["TJ:38", "WTK:2"]),
 "thrips": R(T("蓟马", "Thrips", "Trips"), "p20",
   [T("体长约 1–2 毫米，细长", "About 1–2 mm long and slender", "Kira-kira 1–2 mm panjang dan langsing"), T("翅窄，边缘有长毛", "Narrow wings fringed with long hairs", "Sayap sempit berjumbai bulu panjang")],
   [T("蚜虫：身体圆胖，没有翅毛", "Aphids: plump body, no fringed wings", "Afid: badan gemuk, tiada sayap berjumbai")], ["UMD-THRIPS"]),
 "true-bugs": R(T2("蝽、水黾", "椿象、水黾", "True bugs", "Pepijat"), "p12",
   [T("针管状口器", "Needle-like beak", "Paruh seperti jarum"), T("前翅前半硬、后半膜质", "Forewings hard at base, thin at tip", "Sayap depan keras di pangkal, nipis di hujung")],
   [T("甲虫：前翅全部是硬壳，在背上合成直线", "Beetles: wholly hard forewings meeting in a line", "Kumbang: sayap depan keras sepenuhnya bertemu dalam garis")], ["TJ:39", "WTK:1"]),
 "cicadas-hoppers": R(T("蝉、叶蝉、飞虱、蚜虫", "Cicadas, hoppers and aphids", "Riang-riang, bena dan afid"), "p12",
   [T("针管状口器", "Needle-like beak", "Paruh seperti jarum"), T("翅全部是膜质，停下时像屋顶", "Wholly membranous wings held roof-like", "Sayap bermembran sepenuhnya seperti bumbung")], [], ["TJ:39"]),
 "termites-alates": R(T("白蚁（有翅繁殖蚁）", "Termites (winged swarmers)", "Anai-anai (kelekatu)"), "p18",
   [T("触角念珠状", "Bead-like antennae", "Sesungut seperti manik"), T("四片翅几乎一样大，容易脱落", "Four nearly equal wings that drop off easily", "Empat sayap hampir sama besar yang mudah tanggal")],
   [T("有翅蚂蚁：触角膝状、有细腰、前翅比后翅大", "Winged ants: elbowed antennae, narrow waist, forewings larger", "Semut bersayap: sesungut bersiku, pinggang sempit, sayap depan lebih besar")], ["TJ:39", "WTK:4"]),
 "caddisflies": R(T("石蛾", "Caddisflies", "Lalat kadis"), "p24",
   [T("翅上有细毛", "Hairy wings", "Sayap berbulu"), T("停下时翅呈屋脊状", "Wings held roof-like at rest", "Sayap seperti bumbung ketika berehat"), T("触角细长如线", "Long thread-like antennae", "Sesungut panjang seperti benang")],
   [T("蛾：翅上是鳞片，触角常为羽状或锯齿状", "Moths: scaly wings, often feathery or saw-edged antennae", "Kupu-kupu: sayap bersisik, sesungut selalunya berbulu pelepah atau bergerigi")], ["WTK:8"]),
 "lacewings": R(T("草蛉、蚁蛉、长角蛉", "Lacewings and antlions", "Lacewing dan undur-undur"), "p22",
   [T("翅透明，翅脉多如网", "Clear wings with net-like veins", "Sayap jernih dengan urat seperti jaring"), T("身体柔软", "Soft body", "Badan lembut")],
   [T("豆娘：停下时翅竖起，触角极短", "Damselflies: wings held up, tiny antennae", "Pepatung jarum: sayap tegak, sesungut sangat pendek")], ["TJ:39", "WTK:11"]),
 "ants-alates": R(T("蚂蚁（有翅繁殖蚁）", "Ants (winged)", "Semut (bersayap)"), "p13",
   [T("腰上有一两个结", "One or two nodes on the waist", "Satu atau dua nod pada pinggang"), T("触角膝状", "Elbowed antennae", "Sesungut bersiku")],
   [T("有翅白蚁：触角念珠状、没有细腰", "Winged termites: bead-like antennae, no waist", "Anai-anai bersayap: sesungut seperti manik, tiada pinggang")], ["TJ:39"]),
 "bees-wasps": R(T("蜂类", "Bees and wasps", "Lebah dan tebuan"), "p13",
   [T("有细腰，腰上没有结", "Narrow waist without nodes", "Pinggang sempit tanpa nod"), T("两对膜质翅，前翅较大", "Two pairs of clear wings, forewings larger", "Dua pasang sayap jernih, sayap depan lebih besar")],
   [T("食蚜蝇：只有一对翅，触角短", "Hoverflies: one pair of wings, short antennae", "Lalat bunga: sepasang sayap, sesungut pendek")], ["TJ:39", "WTK:3"]),
 "owlflies": R(T("长角蛉、蚁蛉", "Owlflies and antlions", "Owlfly dan undur-undur"), "p22",
   [T("触角很长，末端膨大", "Long antennae with a knob at the tip", "Sesungut panjang berbonjol di hujung")],
   [T("蜻蜓：触角极短", "Dragonflies: tiny antennae", "Pepatung: sesungut sangat pendek")], ["TJ:39"]),
 "damselflies": R(T("豆娘", "Damselflies", "Pepatung jarum"), "p16",
   [T("四片翅差不多大", "Four similar wings", "Empat sayap yang serupa"), T("停下时翅多合起在背上", "Wings usually closed over the back at rest", "Sayap biasanya tertutup ketika berehat"), T("两眼分开", "Eyes widely separated", "Mata berjauhan")],
   [T("蜻蜓：后翅较宽，停下时平展", "Dragonflies: broader hind wings held flat", "Pepatung: sayap belakang lebih lebar dan terbentang")], ["TJ:39", "WTK:3"]),
 "dragonflies": R(T("蜻蜓", "Dragonflies", "Pepatung"), "p16",
   [T("后翅基部较宽", "Hind wings broader at the base", "Sayap belakang lebih lebar di pangkal"), T("停下时翅平展", "Wings held flat at rest", "Sayap terbentang ketika berehat")],
   [T("豆娘：四翅相似，多合起", "Damselflies: similar wings, usually closed", "Pepatung jarum: sayap serupa, biasanya tertutup")], ["TJ:39", "WTK:3"]),
 "earwigs": R(T("蠼螋", "Earwigs", "Cocopet"), "p21",
   [T("腹末有尾铗", "Pincers at the tip of the abdomen", "Penyepit di hujung abdomen"), T("前翅短小", "Short forewings", "Sayap depan pendek")],
   [T("隐翅虫：前翅也短，但没有尾铗", "Rove beetles: short forewings but no pincers", "Kumbang rove: sayap depan pendek tetapi tiada penyepit")], ["TJ:40", "WTK:7"]),
 "beetles": R(T("甲虫", "Beetles", "Kumbang"), "p10",
   [T("前翅是硬壳（翅鞘）", "Hard forewings (elytra)", "Sayap depan keras (elitra)"), T("两片翅鞘在背中线对齐", "Elytra meet in a straight line down the back", "Elitra bertemu dalam garis lurus di belakang")],
   [T("蝽：前翅后半段是膜质，在背上交叠", "True bugs: forewing tips membranous and overlapping", "Pepijat: hujung sayap depan bermembran dan bertindih")], ["TJ:40", "WTK:1"]),
 "mantids": R(T("螳螂", "Mantids", "Cengkadak"), "p17",
   [T("前足为捕捉足", "Grasping front legs", "Kaki depan penangkap"), T("头呈三角形，可以转动", "Triangular head that can turn", "Kepala segi tiga yang boleh berpusing")],
   [T("竹节虫：前足不是捕捉足", "Stick insects: no grasping front legs", "Serangga ranting: tiada kaki depan penangkap")], ["TJ:40", "WTK:6"]),
 "katydids-crickets": R(T2("螽斯、蟋蟀", "螽蟴、蟋蟀", "Katydids and crickets", "Katidid dan cengkerik"), "p15",
   [T("后足粗大，会跳", "Stout jumping hind legs", "Kaki belakang tegap untuk melompat"), T("触角细长，常比身体长", "Thin antennae, often longer than the body", "Sesungut halus, sering lebih panjang daripada badan")],
   [T("蝗虫：触角短而粗", "Grasshoppers: short thick antennae", "Belalang: sesungut pendek dan tebal")], ["TJ:40", "WTK:5"]),
 "grasshoppers": R(T("蝗虫", "Grasshoppers", "Belalang"), "p15",
   [T("后足粗大，会跳", "Stout jumping hind legs", "Kaki belakang tegap untuk melompat"), T("触角短而粗", "Short, thick antennae", "Sesungut pendek dan tebal")],
   [T("螽斯（台湾称螽蟴）：触角细长", "Katydids: long thin antennae", "Katidid: sesungut panjang halus")], ["TJ:40", "WTK:5"]),
 "mole-crickets": R(T("蝼蛄", "Mole crickets", "Anjing tanah"), "p15",
   [T("前足宽扁像铲子", "Spade-like front legs", "Kaki depan seperti penyodok"), T("住在土里", "Lives in the soil", "Hidup dalam tanah")], [], ["TJ:40"]),
 "cockroaches": R(T("蟑螂", "Cockroaches", "Lipas"), "p18",
   [T("身体扁平", "Flat body", "Badan leper"), T("前胸背板像盾牌盖住头", "Shield-like plate over the head", "Plat seperti perisai menutupi kepala"), T("脚多刺，跑得快", "Spiny legs, runs fast", "Kaki berduri, berlari laju")],
   [T("甲虫：翅鞘在背中线对齐", "Beetles: elytra meet in a straight line", "Kumbang: elitra bertemu dalam garis lurus")], ["TJ:40", "WTK:4"]),
}


if __name__ == "__main__":
    key = {"start": "shape", "nodes": nodes, "results": results}
    Path = __import__("pathlib").Path
    Path("data/key.json").write_text(json.dumps(key, ensure_ascii=False, indent=1) + "\n")
    src = json.loads(Path("data/sources.json").read_text())
    by = {x["id"]: x for x in src}
    by["UMD-THRIPS"] = {"id": "UMD-THRIPS", "short": "UMD Extension: Thrips", "title": "Thrips on flowers",
                        "publisher": "University of Maryland Extension", "url": "https://extension.umd.edu/resource/thrips-flowers", "accessed": "2026-10-21"}
    Path("data/sources.json").write_text(json.dumps(sorted(by.values(), key=lambda x: x["id"]), ensure_ascii=False, indent=1) + "\n")
    print(f"key: {len(nodes)} questions, {len(results)} results")
