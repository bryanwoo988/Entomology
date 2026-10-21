"""p05 — Wings."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, T2, P, L, N, MC, TF, MATCH, FIG, write_chapter
from sources import src

S = ["TJ", "PURDUE-TA"]
chapter = {"id": "p05", "num": 5, "stage": 1, "kind": "lesson",
 "title": T("翅", "Wings", "Sayap"),
 "blurb": T("前翅和后翅、六种翅、平衡棒和小盾片", "Forewings and hind wings, six kinds of wing, halteres and the scutellum", "Sayap depan dan belakang, enam jenis sayap, halter dan skutelum"),
 "sources": S,
 "sections": [
 {"id": "s1", "heading": T("唯一会飞的无脊椎动物", "The only flying invertebrates", "Satu-satunya invertebrata yang terbang"), "level": "basic", "blocks": [
  P("鸟和蝙蝠的翅是由前肢变来的，昆虫的翅却不是。昆虫的翅长在中胸和后胸上：{{t:forewing}}在前，{{t:hindwing}}在后。",
    "Bird and bat wings evolved from front limbs; insect wings did not. They grow from the mesothorax and metathorax: the {{t:forewing|forewings}} in front, the {{t:hindwing|hind wings}} behind.",
    "Sayap burung dan kelawar berasal daripada anggota depan; sayap serangga tidak. Ia tumbuh dari mesotoraks dan metatoraks: {{t:forewing}} di depan, {{t:hindwing}} di belakang.",
    defines=["forewing", "hindwing"], src=["TJ:31"]),
  P("翅除了用来飞，还能保护身体、展示花纹、发出声音和帮助平衡。有些昆虫的一对翅变成了小棒，有些完全没有翅。",
    "Besides flight, wings protect the body, show colour patterns, make sounds and help with balance. In some insects one pair has become tiny knobs; some have no wings at all.",
    "Selain terbang, sayap melindungi badan, mempamerkan corak warna, menghasilkan bunyi dan membantu keseimbangan. Pada sesetengah serangga sepasang sayap menjadi tombol kecil; ada yang langsung tiada sayap.",
    src=["TJ:31"]),
  N("tip", "雄蟋蟀的前翅上有特别的纹路，两片前翅互相摩擦就会发出鸣声。",
    "A male cricket's forewings carry special ridges; rubbing them together makes its song.",
    "Sayap depan cengkerik jantan mempunyai rabung khas; menggeselkannya menghasilkan bunyi nyanyiannya.",
    src=["TJ:30"]),
 ]},
 {"id": "s2", "heading": T("六种翅", "Six kinds of wing", "Enam jenis sayap"), "level": "basic", "blocks": [
  FIG("img/svg/fig-wings.svg", T("示意图：1 鞘翅　2 半鞘翅　3 覆翅　4 鳞翅　5 膜翅　6 平衡棒（红色小球）", "Drawing: 1 elytra, 2 hemelytra, 3 tegmina, 4 scaly wings, 5 membranous wings, 6 halteres (the red knobs)", "Lukisan: 1 elitra, 2 hemelitra, 3 tegmina, 4 sayap bersisik, 5 sayap bermembran, 6 halter (bonjol merah)"), T("示意图", "Six kinds of wing, numbered 1 to 6", "Lukisan")),
  {"type": "keyval", "src": ["TJ:30", "TJ:38", "PURDUE-TA"], "defines": ["elytra", "hemelytra", "tegmina", "halteres"], "rows": [
   {"k": T2("{{t:elytra}}", "{{t:elytra}}", "{{t:elytra|Elytra}}", "{{t:elytra|Elitra}}"), "v": T("甲虫坚硬的前翅，盖住后翅和腹部", "A beetle's hard forewings, covering the hind wings and abdomen", "Sayap depan kumbang yang keras, menutupi sayap belakang dan abdomen")},
   {"k": T("{{t:hemelytra}}", "{{t:hemelytra|Hemelytra}}", "{{t:hemelytra|Hemelitra}}"), "v": T("蝽的前翅：前半段硬、后半段薄而透明", "A true bug's forewings: hard at the base, thin at the tip", "Sayap depan pepijat: keras di pangkal, nipis di hujung")},
   {"k": T("{{t:tegmina}}", "{{t:tegmina|Tegmina}}", "{{t:tegmina|Tegmina}}"), "v": T("像皮革的前翅，如蝗虫、蟑螂、螳螂", "Leathery forewings; grasshoppers, cockroaches, mantids", "Sayap depan seperti kulit; belalang, lipas, cengkadak")},
   {"k": T("鳞翅", "Scaly wings", "Sayap bersisik"), "v": T("盖满彩色鳞片的翅，如蝴蝶和蛾", "Wings covered in coloured scales; butterflies and moths", "Sayap diliputi sisik berwarna; rama-rama dan kupu-kupu")},
   {"k": T("膜翅", "Membranous wings", "Sayap bermembran"), "v": T("薄而透明的翅，如蜂和蜻蜓", "Thin clear wings; bees and dragonflies", "Sayap nipis dan jernih; lebah dan pepatung")},
   {"k": T("{{t:halteres}}", "{{t:halteres|Halteres}}", "{{t:halteres|Halter}}"), "v": T("蝇和蚊的后翅变成的一对小棒，飞行时帮助平衡", "The hind wings of flies and mosquitoes, reduced to knobs that keep them balanced in flight", "Sayap belakang lalat dan nyamuk yang menjadi tombol untuk keseimbangan semasa terbang")}]},
  {"type": "gallery", "ids": ["birdwing-trogonoptera"]},
 ]},
 {"id": "s3", "heading": T2("小盾片", "小楯片", "The scutellum", "Skutelum"), "level": "basic", "blocks": [
  P("{{t:scutellum}}是中胸（或后胸）背面后方的一块小骨片。它的颜色、形状和大小因种类而不同，是辨认的特征之一：蝽的小盾片常是背上的大三角形。",
    "The {{t:scutellum}} is a small plate at the back of the mesothorax (or metathorax), seen from above. Its colour, shape and size vary between kinds and help with identification: in stink bugs it is often a large triangle on the back.",
    "{{t:scutellum}} ialah plat kecil di bahagian belakang mesotoraks (atau metatoraks), dilihat dari atas. Warna, bentuk dan saiznya berbeza mengikut jenis dan membantu pengecaman: pada pepijat busuk ia sering segi tiga besar di belakang.",
    defines=["scutellum"], src=["TJ:31"]),
  {"type": "gallery", "ids": ["shield-bug-tetrarthria"]},
 ]},
]}

terms = [
 ("forewing", T("前翅", "Forewing", "Sayap depan"), T("长在中胸上的一对翅。", "The pair of wings on the mesothorax.", "Sepasang sayap pada mesotoraks.")),
 ("hindwing", T("后翅", "Hind wing", "Sayap belakang"), T("长在后胸上的一对翅。", "The pair of wings on the metathorax.", "Sepasang sayap pada metatoraks.")),
 ("elytra", T2("鞘翅", "翅鞘", "Elytra", "Elitra"), T("甲虫坚硬的前翅，在背中线对齐。", "A beetle's hard forewings, meeting in a line down the back.", "Sayap depan kumbang yang keras, bertemu dalam garis di belakang.")),
 ("hemelytra", T("半鞘翅", "Hemelytra", "Hemelitra"), T("蝽的前翅，前半段硬、后半段膜质。", "A true bug's forewing, hard at the base and membranous at the tip.", "Sayap depan pepijat, keras di pangkal dan bermembran di hujung.")),
 ("tegmina", T("覆翅", "Tegmina", "Tegmina"), T("像皮革一样的前翅，如蝗虫和蟑螂。", "Leathery forewings, as in grasshoppers and cockroaches.", "Sayap depan seperti kulit, seperti belalang dan lipas.")),
 ("halteres", T("平衡棒", "Halteres", "Halter"), T("蝇和蚊的后翅变成的小棒，帮助平衡。", "The knob-like hind wings of flies, used for balance.", "Sayap belakang lalat yang menjadi tombol untuk keseimbangan.")),
 ("scutellum", T2("小盾片", "小楯片", "Scutellum", "Skutelum"), T("胸部背面后方的一块小骨片。", "A small plate at the back of the thorax, seen from above.", "Plat kecil di bahagian belakang toraks, dilihat dari atas.")),
]

quiz = [
 MC(T("甲虫坚硬的前翅叫什么？", "What are a beetle's hard forewings called?", "Apakah nama sayap depan kumbang yang keras?"), [T("覆翅", "Tegmina", "Tegmina"), T2("鞘翅", "翅鞘", "Elytra", "Elitra"), T("半鞘翅", "Hemelytra", "Hemelitra")], 1,
    T("甲虫的前翅是鞘翅。", "A beetle's forewings are elytra.", "Sayap depan kumbang ialah elitra."), ["TJ:30"]),
 MC(T("哪一类昆虫的后翅变成平衡棒？", "Which insects have hind wings reduced to halteres?", "Serangga manakah yang sayap belakangnya menjadi halter?"), [T("蝇和蚊", "Flies and mosquitoes", "Lalat dan nyamuk"), T("蜜蜂", "Bees", "Lebah"), T("蝴蝶", "Butterflies", "Rama-rama")], 0,
    T("双翅目的后翅变成了平衡棒。", "In flies (Diptera) the hind wings are halteres.", "Pada lalat (Diptera) sayap belakang menjadi halter."), ["TJ:38", "PURDUE-TA"]),
 TF(T("昆虫的翅和鸟一样，是由前肢变来的。", "Insect wings, like bird wings, evolved from front limbs.", "Sayap serangga, seperti sayap burung, berasal daripada anggota depan."), False,
    T("昆虫的翅不是由前肢变来的。", "Insect wings did not come from limbs.", "Sayap serangga tidak berasal daripada anggota badan."), ["TJ:31"]),
 MATCH(T("把翅和昆虫配对。", "Match the wing to the insect.", "Padankan sayap dengan serangga."),
    [(T2("鞘翅", "翅鞘", "Elytra", "Elitra"), T("甲虫", "Beetle", "Kumbang")), (T("半鞘翅", "Hemelytra", "Hemelitra"), T("蝽", "Stink bug", "Pepijat busuk")), (T("鳞翅", "Scaly wings", "Sayap bersisik"), T("蝴蝶", "Butterfly", "Rama-rama"))],
    T("甲虫是鞘翅，蝽是半鞘翅，蝴蝶是鳞翅。", "Beetles: elytra; bugs: hemelytra; butterflies: scaly wings.", "Kumbang: elitra; pepijat: hemelitra; rama-rama: sayap bersisik."), ["TJ:30"]),
]

write_chapter(chapter, terms, src(*S), quiz)
