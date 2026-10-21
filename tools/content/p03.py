"""p03 — The head."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, T2, P, L, N, MC, TF, MATCH, write_chapter
from sources import src

S = ["TJ", "AES-ANT", "WTK"]
chapter = {"id": "p03", "num": 3, "stage": 1, "kind": "lesson",
 "title": T("头部：触角、眼睛和口器", "The head: antennae, eyes and mouthparts", "Kepala: sesungut, mata dan bahagian mulut"),
 "blurb": T("触角的七种形状、复眼和单眼、五种口器", "Seven antenna shapes, compound eyes and ocelli, five kinds of mouthparts", "Tujuh bentuk sesungut, mata majmuk dan oselus, lima jenis bahagian mulut"),
 "sources": S,
 "sections": [
 {"id": "s1", "heading": T("感觉的中心", "The centre of the senses", "Pusat deria"), "level": "basic", "blocks": [
  P("头部有一对触角、一对复眼、零到三个单眼，和一组口器。",
    "The head carries a pair of antennae, a pair of compound eyes, up to three simple eyes, and a set of mouthparts.",
    "Kepala mempunyai sepasang sesungut, sepasang mata majmuk, sehingga tiga mata ringkas, dan satu set bahagian mulut.",
    src=["TJ:25"]),
  P("{{t:antenna}}长在头的前面，上面有很多感觉器，可以摸、闻、尝，有的还能听。它分三段：基部的柄节、中间的梗节和最长的鞭节。",
    "The {{t:antenna}} sits at the front of the head and is covered with sense organs for touch, smell and taste, and in some insects hearing. It has three parts: the scape at the base, the pedicel, and the long flagellum.",
    "{{t:antenna}} terletak di hadapan kepala dan dipenuhi organ deria untuk sentuhan, bau dan rasa, malah pendengaran bagi sesetengah serangga. Ia ada tiga bahagian: skap di pangkal, pedisel, dan flagelum yang panjang.",
    defines=["antenna"], src=["TJ:25"]),
  P("{{t:compound-eye}}由许多小眼组成。眼睛越大，小眼越多，看得越清楚：蜻蜓的复眼很大，蚂蚁的很小。",
    "A {{t:compound-eye}} is made of many small units. The larger the eye, the more units and the sharper the sight: dragonflies have huge compound eyes, ants small ones.",
    "{{t:compound-eye}} terdiri daripada banyak unit kecil. Lebih besar mata, lebih banyak unit dan lebih jelas penglihatan: pepatung bermata majmuk besar, semut kecil.",
    defines=["compound-eye"], src=["TJ:27"]),
  P("{{t:ocellus}}通常在两个复眼之间，最多三个，只分得出明暗，帮助复眼看东西。有些昆虫没有单眼。",
    "An {{t:ocellus}} (simple eye) usually sits between the compound eyes; there are at most three. It senses light and dark and helps the compound eyes. Some insects have none.",
    "{{t:ocellus}} (mata ringkas) biasanya terletak di antara mata majmuk; paling banyak tiga. Ia mengesan terang dan gelap dan membantu mata majmuk. Sesetengah serangga tiada oselus.",
    defines=["ocellus"], src=["TJ:25"]),
 ]},
 {"id": "s2", "heading": T("触角的形状", "Antenna shapes", "Bentuk sesungut"), "level": "basic", "blocks": [
  P("触角的形状常常能帮你分辨昆虫的类群：",
    "The shape of the antennae often tells you which group an insect belongs to:",
    "Bentuk sesungut sering menunjukkan kumpulan serangga itu:",
    src=["AES-ANT", "TJ:38"]),
  {"type": "keyval", "src": ["AES-ANT", "TJ:38", "WTK:2", "WTK:5"], "defines": ["moniliform", "geniculate"], "rows": [
   {"k": T("丝状", "Filiform (thread-like)", "Filiform (seperti benang)"), "v": T("许多大小差不多的小节连成细线，如螽斯、蟋蟀", "Many similar segments forming a thin thread; katydids, crickets", "Banyak ruas serupa membentuk benang halus; katidid, cengkerik")},
   {"k": T("{{t:moniliform}}", "{{t:moniliform|Moniliform (bead-like)}}", "{{t:moniliform|Moniliform (seperti manik)}}"), "v": T("一节节圆珠，像一串念珠，如白蚁", "Round segments like a string of beads; termites", "Ruas bulat seperti rantai manik; anai-anai")},
   {"k": T("{{t:geniculate}}", "{{t:geniculate|Geniculate (elbowed)}}", "{{t:geniculate|Genikulat (bersiku)}}"), "v": T("中间折成一个角，像手肘，如蚂蚁和一些蜂", "Bent sharply in the middle like an elbow; ants and some bees", "Bengkok tajam di tengah seperti siku; semut dan sesetengah lebah")},
   {"k": T("棍棒状", "Clavate (clubbed)", "Klavat (berbonjol)"), "v": T("末端渐渐或突然变粗，如蝴蝶", "Thickening towards the tip; butterflies", "Menebal ke hujung; rama-rama")},
   {"k": T("锯齿状", "Serrate (saw-edged)", "Serat (bergerigi)"), "v": T("每节一边突出，像锯子边", "Each segment juts out on one side like a saw", "Setiap ruas menonjol pada satu sisi seperti gergaji")},
   {"k": T("栉齿状、羽状", "Pectinate, plumose (comb-like, feathery)", "Pektinat, plumos (seperti sikat, berbulu pelepah)"), "v": T("一边或两边有长突起，像梳子或羽毛，如许多蛾", "Long side branches like a comb or feather; many moths", "Cabang sisi panjang seperti sikat atau bulu pelepah; banyak kupu-kupu")},
   {"k": T("鳃叶状", "Lamellate (plate-tipped)", "Lamelat (berlamela)"), "v": T("末端几节变成可以张开的薄片，如金龟", "The last segments are flat plates that can fan out; scarab beetles", "Ruas hujung menjadi kepingan leper yang boleh dikembangkan; kumbang skarab")}]},
 ]},
 {"id": "s3", "heading": T("口器", "Mouthparts", "Bahagian mulut"), "level": "basic", "blocks": [
  P("{{t:mouthparts}}有五个基本部分：上唇、大颚、小颚、下唇和舌。不同的昆虫吃不同的食物，口器也变成不同的样子：",
    "{{t:mouthparts}} have five basic parts: the upper lip (labrum), mandibles, maxillae, lower lip (labium) and tongue (hypopharynx). Insects that eat different food have mouthparts of different shapes:",
    "{{t:mouthparts}} mempunyai lima bahagian asas: bibir atas (labrum), mandibel, maksila, bibir bawah (labium) dan lidah (hipofarinks). Serangga yang makan makanan berbeza mempunyai bahagian mulut yang berbeza bentuk:",
    defines=["mouthparts"], src=["TJ:27"]),
  {"type": "keyval", "src": ["TJ:27"], "defines": ["piercing-sucking"], "rows": [
   {"k": T("咀嚼式", "Chewing", "Mengunyah"), "v": T("用大颚咬碎食物，如土蜂", "Mandibles bite and grind food; scoliid wasps", "Mandibel menggigit dan mengunyah makanan; tebuan skolid")},
   {"k": T2("嚼吸式", "咀吸式", "Chewing-lapping", "Mengunyah-menjilat"), "v": T("既能咬也能舔吸花蜜，如许多蜂", "Can both bite and lap up nectar; many bees and wasps", "Boleh menggigit dan menjilat nektar; banyak lebah dan tebuan")},
   {"k": T2("舐吸式", "舐吮式", "Sponging", "Menyerap"), "v": T("用海绵状的口器吸取液体，如果实蝇", "A sponge-like pad soaks up liquids; fruit flies", "Pad seperti span menyerap cecair; lalat buah")},
   {"k": T("虹吸式", "Siphoning", "Menyedut (sifon)"), "v": T("一根卷起来的长吸管，如蝴蝶", "A long coiled tube; butterflies", "Tiub panjang bergulung; rama-rama")},
   {"k": T("{{t:piercing-sucking}}", "{{t:piercing-sucking|Piercing-sucking}}", "{{t:piercing-sucking|Menusuk-menghisap}}"), "v": T("针管状，刺进植物或动物吸汁，如蝽", "A needle-like beak that pierces plants or animals and sucks; stink bugs", "Paruh seperti jarum yang menusuk tumbuhan atau haiwan dan menghisap; pepijat busuk")}]},
  N("key", "看口器就能猜到它吃什么、怎样危害作物：刺吸式的害虫（蚜虫、飞虱）吸汁，咀嚼式的（毛虫、甲虫）把叶子咬出洞。",
    "Mouthparts tell you how an insect feeds and how it harms crops: piercing-sucking pests (aphids, planthoppers) suck sap; chewing pests (caterpillars, beetles) bite holes in leaves.",
    "Bahagian mulut menunjukkan cara serangga makan dan merosakkan tanaman: perosak menusuk-menghisap (afid, bena perang) menghisap cecair; perosak mengunyah (ulat, kumbang) menggigit daun hingga berlubang.",
    src=["TJ:27", "TJ:39"]),
 ]},
]}

terms = [
 ("antenna", T("触角", "Antenna", "Sesungut"), T("头前面一对分节的感觉器官，能摸、闻、尝。", "A pair of jointed feelers on the head, used to touch, smell and taste.", "Sepasang organ deria beruas di kepala untuk menyentuh, menghidu dan merasa.")),
 ("compound-eye", T("复眼", "Compound eye", "Mata majmuk"), T("由许多小眼组成的大眼睛。", "A large eye made of many small units.", "Mata besar yang terdiri daripada banyak unit kecil.")),
 ("ocellus", T("单眼", "Ocellus (simple eye)", "Oselus (mata ringkas)"), T("复眼之间的小眼睛，最多三个，感受明暗。", "A small eye between the compound eyes, at most three, sensing light and dark.", "Mata kecil di antara mata majmuk, paling banyak tiga, mengesan terang dan gelap.")),
 ("moniliform", T("念珠状触角", "Moniliform antenna", "Sesungut moniliform"), T("像一串圆珠的触角，白蚁有这种触角。", "A bead-like antenna, as in termites.", "Sesungut seperti rantai manik, seperti pada anai-anai.")),
 ("geniculate", T2("膝状触角", "屈膝状触角", "Geniculate antenna", "Sesungut genikulat"), T("中间折成一个角的触角，蚂蚁有这种触角。", "An antenna bent like an elbow, as in ants.", "Sesungut yang bengkok seperti siku, seperti pada semut.")),
 ("mouthparts", T("口器", "Mouthparts", "Bahagian mulut"), T("昆虫用来取食的一组构造。", "The set of parts an insect feeds with.", "Set bahagian yang digunakan serangga untuk makan.")),
 ("piercing-sucking", T("刺吸式口器", "Piercing-sucking mouthparts", "Bahagian mulut menusuk-menghisap"), T("像针管的口器，刺进植物或动物吸汁。", "Needle-like mouthparts that pierce and suck fluids.", "Bahagian mulut seperti jarum yang menusuk dan menghisap cecair.")),
]

quiz = [
 MC(T("蚂蚁的触角是什么形状？", "What shape are an ant's antennae?", "Apakah bentuk sesungut semut?"), [T("丝状", "Thread-like", "Seperti benang"), T("膝状", "Elbowed", "Bersiku"), T("鳃叶状", "Plate-tipped", "Berlamela")], 1,
    T("蚂蚁的触角在中间折成膝状。", "Ant antennae bend like an elbow.", "Sesungut semut bengkok seperti siku."), ["AES-ANT", "TJ:38"]),
 MC(T("哪一个只分得出明暗、帮助复眼？", "Which only senses light and dark, helping the compound eyes?", "Yang manakah hanya mengesan terang dan gelap, membantu mata majmuk?"), [T("单眼", "Ocellus", "Oselus"), T("触角", "Antenna", "Sesungut"), T("上唇", "Labrum", "Labrum")], 0,
    T("单眼感受光线强弱，在视觉上做辅助。", "Ocelli sense light intensity and support the compound eyes.", "Oselus mengesan keamatan cahaya dan membantu mata majmuk."), ["TJ:25"]),
 MATCH(T("把口器和昆虫配对。", "Match the mouthparts to the insect.", "Padankan bahagian mulut dengan serangga."),
    [(T("刺吸式", "Piercing-sucking", "Menusuk-menghisap"), T("蝽", "Stink bug", "Pepijat busuk")),
     (T("虹吸式", "Siphoning", "Menyedut"), T("蝴蝶", "Butterfly", "Rama-rama")),
     (T2("舐吸式", "舐吮式", "Sponging", "Menyerap"), T("果实蝇", "Fruit fly", "Lalat buah"))],
    T("蝽刺吸、蝴蝶虹吸、果实蝇舐吸。", "Stink bugs pierce and suck, butterflies siphon, fruit flies sponge.", "Pepijat busuk menusuk, rama-rama menyedut, lalat buah menyerap."), ["TJ:27"]),
]

write_chapter(chapter, terms, src(*S), quiz)
