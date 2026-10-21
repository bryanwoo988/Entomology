"""p09 — Life cycles."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, T2, P, L, N, MC, TF, MATCH, PHOTO, write_chapter
from sources import src

S = ["TJ", "NCSU-META", "LCWU-META", "RS12", "RS34"]
chapter = {"id": "p09", "num": 9, "stage": 3, "kind": "lesson",
 "title": T("生活史", "Life cycles", "Kitaran hidup"),
 "blurb": T("蜕皮、三种发育方式、幼虫和蛹的样子，以及为什么防治要看虫期", "Moulting, three ways of growing up, what larvae and pupae look like, and why pest control depends on the stage", "Salin kulit, tiga cara membesar, rupa larva dan pupa, dan mengapa kawalan perosak bergantung pada peringkat"),
 "sources": S,
 "sections": [
 {"id": "s1", "heading": T("长大要蜕皮", "Growing means moulting", "Membesar bermakna bersalin kulit"), "level": "basic", "blocks": [
  P("昆虫的外骨骼不会跟着长大，所以要定期{{t:moult}}，换上一层新的、较大的外皮。每蜕一次皮，就进入下一个{{t:instar}}。",
    "An insect's exoskeleton cannot grow, so the insect must {{t:moult}} from time to time and grow a new, larger skin. Each moult starts a new {{t:instar}}.",
    "Rangka luar serangga tidak boleh membesar, jadi serangga mesti {{t:moult}} dari semasa ke semasa dan membentuk kulit baharu yang lebih besar. Setiap salin kulit memulakan {{t:instar}} baharu.",
    defines=["moult", "instar"], src=["TJ:34"]),
 ]},
 {"id": "s2", "heading": T("三种发育方式", "Three ways of growing up", "Tiga cara membesar"), "level": "basic", "blocks": [
  P("{{t:ametabolous}}：从卵孵出来就像缩小的成虫，长大后仍会继续蜕皮。例如衣鱼和石蛃。",
    "{{t:ametabolous|No metamorphosis}}: the young hatch looking like small adults and keep moulting even after they mature, as in silverfish and bristletails.",
    "{{t:ametabolous|Tanpa metamorfosis}}: anak yang menetas kelihatan seperti dewasa kecil dan terus bersalin kulit selepas matang, seperti gegat dan bristletail.",
    defines=["ametabolous"], src=["TJ:34"]),
  P("{{t:incomplete-metamorphosis}}：卵 → {{t:nymph}} → 成虫。若虫有翅芽，生活方式和成虫差不多，最后一次蜕皮才长出完整的翅。住在水里的若虫又叫稚虫。",
    "{{t:incomplete-metamorphosis}}: egg → {{t:nymph}} → adult. Nymphs have wing buds and live much like the adults; full wings appear at the last moult. Water-dwelling nymphs are also called naiads.",
    "{{t:incomplete-metamorphosis}}: telur → {{t:nymph}} → dewasa. Nimfa mempunyai tunas sayap dan hidup hampir sama seperti dewasa; sayap penuh muncul pada salin kulit terakhir. Nimfa yang hidup dalam air juga dipanggil naiad.",
    defines=["incomplete-metamorphosis", "nymph"], src=["TJ:35"]),
  P("这样发育的有：蜉蝣目、蜻蜓目、直翅目、蜚蠊目（包括白蚁）、半翅目、螳螂目、竹节虫目、革翅目、襀翅目、纺足目、缨翅目等。",
    "Insects that grow this way include mayflies, dragonflies, grasshoppers and crickets, cockroaches (termites included), true bugs and hoppers, mantids, stick insects, earwigs, stoneflies, webspinners and thrips.",
    "Serangga yang membesar begini termasuk lalat sehari, pepatung, belalang dan cengkerik, lipas (termasuk anai-anai), pepijat dan bena, cengkadak, serangga ranting, cocopet, lalat batu, labah-labah sutera dan trips.",
    src=["TJ:35"]),
  P("{{t:complete-metamorphosis}}：卵 → {{t:larva}} → {{t:pupa}} → 成虫。幼虫和成虫的样子、食物和住处常常完全不同；身体在蛹里重新组合。",
    "{{t:complete-metamorphosis}}: egg → {{t:larva}} → {{t:pupa}} → adult. Larvae and adults often differ completely in shape, food and home; the body is rebuilt inside the pupa.",
    "{{t:complete-metamorphosis}}: telur → {{t:larva}} → {{t:pupa}} → dewasa. Larva dan dewasa sering berbeza sepenuhnya dari segi bentuk, makanan dan tempat tinggal; badan dibina semula di dalam pupa.",
    defines=["complete-metamorphosis", "larva", "pupa"], src=["TJ:35"]),
  P("这样发育的有：鞘翅目、鳞翅目、双翅目、膜翅目、脉翅目、广翅目、蛇蛉目、毛翅目、长翅目、蚤目和捻翅目。",
    "Insects that grow this way include beetles, butterflies and moths, flies, bees, wasps and ants, lacewings, alderflies and dobsonflies, snakeflies, caddisflies, scorpionflies, fleas and twisted-wing parasites.",
    "Serangga yang membesar begini termasuk kumbang, rama-rama dan kupu-kupu, lalat, lebah, tebuan dan semut, lacewing, alderfly, snakefly, lalat kadis, lalat kala jengking, kutu dan parasit bersayap terpiuh.",
    src=["TJ:35"]),
 ]},
 {"id": "s3", "heading": T("幼虫和蛹的样子", "What larvae and pupae look like", "Rupa larva dan pupa"), "level": "basic", "blocks": [
  {"type": "keyval", "src": ["NCSU-META", "LCWU-META"], "rows": [
   {"k": T("蠋型幼虫", "Caterpillar-like (eruciform)", "Seperti ulat (eruciform)"), "v": T("三对胸足，腹部还有几对肉质的腹足；如蝴蝶和蛾的毛虫", "Three pairs of true legs plus fleshy prolegs on the abdomen; caterpillars of butterflies and moths", "Tiga pasang kaki sebenar serta kaki palsu berisi pada abdomen; ulat rama-rama dan kupu-kupu")},
   {"k": T("蛴螬型幼虫", "Grub-like (scarabaeiform)", "Seperti gendon (scarabaeiform)"), "v": T("身体弯成 C 形，胸足短，行动慢，住在土里或木头里；如金龟和犀角金龟", "C-shaped with short legs, slow, living in soil or wood; scarab and rhinoceros beetles", "Berbentuk C dengan kaki pendek, perlahan, hidup dalam tanah atau kayu; kumbang skarab dan kumbang badak")},
   {"k": T("无足型幼虫（蛆）", "Legless (vermiform), maggots", "Tanpa kaki (vermiform), berenga"), "v": T("没有脚，如家蝇的蛆", "No legs at all; house-fly maggots", "Tiada kaki langsung; berenga lalat rumah")},
   {"k": T("被蛹", "Obtect pupa", "Pupa obtek"), "v": T("触角、脚和翅芽都贴在身上；如蛾和蝴蝶", "Antennae, legs and wing pads glued to the body; moths and butterflies", "Sesungut, kaki dan pad sayap melekat pada badan; kupu-kupu dan rama-rama")},
   {"k": T("离蛹", "Exarate pupa", "Pupa eksarat"), "v": T("附肢离开身体、看得见；如蜂", "Appendages free and visible; bees and wasps", "Anggota bebas dan kelihatan; lebah dan tebuan")},
   {"k": T("围蛹", "Coarctate pupa (puparium)", "Pupa koarktat (puparium)"), "v": T("包在最后一龄幼虫变硬的皮里，像小桶；如蝇", "Inside the hardened last larval skin, like a small barrel; flies", "Di dalam kulit larva terakhir yang mengeras, seperti tong kecil; lalat")}]},
 ]},
 {"id": "s4", "heading": T("为什么农民要懂生活史", "Why farmers need to know life cycles", "Mengapa petani perlu tahu kitaran hidup"), "level": "basic", "blocks": [
  P("很多害虫是在幼虫期吃作物，成虫反而不吃。油棕的袋蛾就是这样：Metisa plana 的幼虫躲在用叶片做的袋子里吃叶子，一个世代大约 90 天。",
    "Many pests damage crops as larvae, not as adults. Oil palm bagworms are an example: larvae of Metisa plana feed on the fronds from inside bags made of leaf pieces, and one generation takes about 90 days.",
    "Banyak perosak merosakkan tanaman semasa peringkat larva, bukan dewasa. Ulat bungkus sawit ialah contohnya: larva Metisa plana makan pelepah dari dalam bungkus daripada cebisan daun, dan satu generasi mengambil kira-kira 90 hari.",
    src=["RS12:1-3", "RS34:2"]),
  PHOTO("metisa-plana-early-larvae"),
  PHOTO("metisa-plana-late-larvae"),
  PHOTO("metisa-plana-pupa-bag"),
  PHOTO("metisa-plana-adult-male"),
  P("MPOB 建议在幼虫的早期和中期进行化学防治；在卵期（卵藏在雌虫的袋里）、晚期幼虫和蛹期，应暂缓用药。同一种药，用对了虫期才有效。",
    "MPOB advises chemical control during the early and middle larval stages, and holding off during the egg stage (eggs are kept inside the female's bag), the late larval stage and the pupal stage. The same treatment only works at the right stage.",
    "MPOB menasihatkan kawalan kimia semasa peringkat larva awal dan pertengahan, dan menangguhkannya semasa peringkat telur (telur disimpan dalam bungkus betina), larva lewat dan pupa. Rawatan yang sama hanya berkesan pada peringkat yang betul.",
    src=["RS12:3"]),
 ]},
]}

terms = [
 ("moult", T("蜕皮", "Moult", "Salin kulit"), T("脱去旧的外骨骼、换上较大的新外皮。", "Shedding the old exoskeleton for a new, larger one.", "Menanggalkan rangka luar lama untuk yang baharu dan lebih besar.")),
 ("instar", T("龄期", "Instar", "Instar"), T("两次蜕皮之间的生长阶段。", "A growth stage between two moults.", "Peringkat pertumbuhan antara dua salin kulit.")),
 ("ametabolous", T("无变态", "No metamorphosis (ametabolous)", "Tanpa metamorfosis (ametabola)"), T("幼体和成虫外形相同，只是变大。", "Young look like small adults and just grow.", "Anak kelihatan seperti dewasa kecil dan hanya membesar.")),
 ("incomplete-metamorphosis", T("不完全变态", "Incomplete metamorphosis", "Metamorfosis tidak lengkap"), T("卵、若虫、成虫三个阶段，没有蛹。", "Egg, nymph, adult; no pupa.", "Telur, nimfa, dewasa; tiada pupa.")),
 ("nymph", T("若虫", "Nymph", "Nimfa"), T("不完全变态昆虫的幼体，有翅芽。", "The young of an insect with incomplete metamorphosis; it has wing buds.", "Anak serangga dengan metamorfosis tidak lengkap; ia mempunyai tunas sayap.")),
 ("complete-metamorphosis", T("完全变态", "Complete metamorphosis", "Metamorfosis lengkap"), T("卵、幼虫、蛹、成虫四个阶段。", "Egg, larva, pupa, adult.", "Telur, larva, pupa, dewasa.")),
 ("larva", T("幼虫", "Larva", "Larva"), T("完全变态昆虫的幼体，样子和成虫很不一样。", "The young of an insect with complete metamorphosis, unlike the adult.", "Anak serangga dengan metamorfosis lengkap, berbeza daripada dewasa.")),
 ("pupa", T("蛹", "Pupa", "Pupa"), T("幼虫变成成虫之前的休息阶段。", "The resting stage between larva and adult.", "Peringkat rehat antara larva dan dewasa.")),
]

quiz = [
 MC(T("完全变态的四个阶段，顺序是？", "The four stages of complete metamorphosis, in order?", "Empat peringkat metamorfosis lengkap, mengikut urutan?"),
    [T("卵 → 若虫 → 成虫 → 蛹", "Egg → nymph → adult → pupa", "Telur → nimfa → dewasa → pupa"), T("卵 → 幼虫 → 蛹 → 成虫", "Egg → larva → pupa → adult", "Telur → larva → pupa → dewasa"), T("幼虫 → 卵 → 蛹 → 成虫", "Larva → egg → pupa → adult", "Larva → telur → pupa → dewasa")], 1,
    T("卵、幼虫、蛹、成虫。", "Egg, larva, pupa, adult.", "Telur, larva, pupa, dewasa."), ["TJ:35"]),
 MC(T("蝗虫是哪一种发育方式？", "How do grasshoppers grow up?", "Bagaimana belalang membesar?"), [T("不完全变态", "Incomplete metamorphosis", "Metamorfosis tidak lengkap"), T("完全变态", "Complete metamorphosis", "Metamorfosis lengkap"), T("无变态", "No metamorphosis", "Tanpa metamorfosis")], 0,
    T("直翅目是不完全变态：卵、若虫、成虫。", "Orthoptera: egg, nymph, adult.", "Orthoptera: telur, nimfa, dewasa."), ["TJ:35"]),
 MC(T("袋蛾什么时候用药效果最好？", "When does chemical control of bagworms work best?", "Bilakah kawalan kimia ulat bungkus paling berkesan?"), [T("卵期", "Egg stage", "Peringkat telur"), T("幼虫早期和中期", "Early and middle larvae", "Larva awal dan pertengahan"), T("蛹期", "Pupal stage", "Peringkat pupa")], 1,
    T("MPOB 建议在幼虫早期和中期用药。", "MPOB advises treating early and middle larvae.", "MPOB menasihatkan rawatan pada larva awal dan pertengahan."), ["RS12:3"]),
 MATCH(T("把幼虫类型和昆虫配对。", "Match the larva to the insect.", "Padankan larva dengan serangga."),
    [(T("蛴螬型", "Grub-like", "Seperti gendon"), T("犀角金龟", "Rhinoceros beetle", "Kumbang badak")), (T("蠋型", "Caterpillar-like", "Seperti ulat"), T("蛾", "Moth", "Kupu-kupu")), (T("无足型", "Legless", "Tanpa kaki"), T("家蝇", "House fly", "Lalat rumah"))],
    T("金龟的幼虫是蛴螬型，蛾是蠋型，蝇是无足的蛆。", "Beetle grubs, moth caterpillars, fly maggots.", "Gendon kumbang, ulat kupu-kupu, berenga lalat."), ["NCSU-META", "LCWU-META"]),
]

write_chapter(chapter, terms, src(*S), quiz)
