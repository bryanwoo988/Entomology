"""p08 — Identifying with a key."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, T2, P, L, N, MC, TF, MATCH, write_chapter
from sources import src

S = ["TJ"]
chapter = {"id": "p08", "num": 8, "stage": 2, "kind": "lesson",
 "title": T("用检索表辨识", "Identifying with a key", "Mengecam dengan kunci"),
 "blurb": T("二分检索表怎样一步步缩小范围，以及用图练习", "How a dichotomous key narrows things down, with picture practice", "Bagaimana kunci dikotomi mengecilkan pilihan, dengan latihan bergambar"),
 "sources": S,
 "sections": [
 {"id": "s1", "heading": T("一步一个问题", "One question at a time", "Satu soalan pada satu masa"), "level": "basic", "blocks": [
  P("{{t:dichotomous-key}}每一步只问一个看得见的特征，给你两个（或几个）选项。每答一题就排除一部分昆虫，几步之后就剩下一个类群。",
    "A {{t:dichotomous-key}} asks about one visible feature at each step and gives two (or a few) choices. Each answer rules out some insects, and after a few steps only one group is left.",
    "{{t:dichotomous-key}} bertanya tentang satu ciri yang boleh dilihat pada setiap langkah dan memberi dua (atau beberapa) pilihan. Setiap jawapan menyingkirkan sebahagian serangga, dan selepas beberapa langkah hanya satu kumpulan yang tinggal.",
    defines=["dichotomous-key"], src=["TJ:40"]),
  P("这个 App 底部的「辨识」就是这样一张检索表，根据台江图鉴的检索表，再加上马来西亚常见的竹节虫、蜉蝣、石蛾、蓟马和衣鱼。",
    "The Identify button at the bottom of this app is such a key. It follows the Taijiang guide's key, with Malaysia's common stick insects, mayflies, caddisflies, thrips and silverfish added.",
    "Butang Kenal pasti di bahagian bawah aplikasi ini ialah kunci seperti itu. Ia mengikut kunci panduan Taijiang, dengan tambahan serangga ranting, lalat sehari, lalat kadis, trips dan gegat yang biasa di Malaysia.",
    src=["TJ:38-40"]),
  L(("用放大镜，从侧面和背面都看一看", "Use a hand lens and look from the side and from above", "Gunakan kanta pembesar dan lihat dari sisi dan dari atas"),
    ("看不清楚就选「看不清楚」，读提示，不要猜", "If you can't tell, choose Can't tell and read the hint rather than guess", "Jika tidak pasti, pilih Tidak pasti dan baca petunjuk, jangan meneka"),
    ("得到结果后，逐项核对它的特征", "When you get a result, check its features one by one", "Apabila mendapat keputusan, semak cirinya satu demi satu"),
    src=["TJ:38-40"]),
  N("warn", "检索表只适用于常见昆虫的成虫，有许多例外；精确的鉴定仍要请教专家。",
    "A key works only for adults of common insects and has many exceptions; ask an expert for a firm identification.",
    "Kunci hanya sesuai untuk serangga dewasa yang biasa dan mempunyai banyak pengecualian; rujuk pakar untuk pengecaman yang pasti.",
    src=["TJ:40"]),
 ]},
 {"id": "s2", "heading": T("看图练习", "Picture practice", "Latihan bergambar"), "level": "basic", "blocks": [
  P("这一页的小测验用检索表里的示意图练习：每张图左边是「是」，右边是「不是」。",
    "This page's quiz practises with the key's drawings: in each picture the left side shows 'yes' and the right side 'no'.",
    "Kuiz halaman ini berlatih dengan lukisan kunci: dalam setiap gambar, sebelah kiri menunjukkan 'ya' dan sebelah kanan 'tidak'.",
    src=["TJ:38-40"]),
 ]},
]}

terms = [
 ("dichotomous-key", T("二分检索表", "Dichotomous key", "Kunci dikotomi"), T("每一步用一个特征把选项分开、逐步缩小范围的辨识工具。", "An identification tool that splits the choices by one feature at each step.", "Alat pengecaman yang membahagikan pilihan mengikut satu ciri pada setiap langkah.")),
]

quiz = [
 MC(T("左图的前翅是硬壳，在背中央对齐。这是哪一目？", "On the left, the forewings are hard shells meeting down the middle. Which order?", "Di kiri, sayap depan ialah cangkerang keras yang bertemu di tengah. Order apa?"),
    [T("鞘翅目", "Coleoptera (beetles)", "Coleoptera (kumbang)"), T("半翅目", "Hemiptera (bugs)", "Hemiptera (pepijat)"), T("直翅目", "Orthoptera (grasshoppers)", "Orthoptera (belalang)")], 0,
    T("翅鞘在背中线对齐是甲虫的特征。", "Elytra meeting in a straight line mark a beetle.", "Elitra yang bertemu dalam garis lurus menandakan kumbang."), ["TJ:40"], img="img/svg/key-elytra.svg"),
 MC(T("左图的前足像镰刀。这是哪一类昆虫？", "On the left, the front legs are like folding blades. Which insect?", "Di kiri, kaki depan seperti pisau lipat. Serangga apa?"),
    [T("蟑螂", "Cockroach", "Lipas"), T("螳螂", "Mantis", "Cengkadak"), T("蝼蛄", "Mole cricket", "Anjing tanah")], 1,
    T("捕捉足是螳螂的特征。", "Grasping front legs mark a mantis.", "Kaki depan penangkap menandakan cengkadak."), ["TJ:40"], img="img/svg/key-raptorial.svg"),
 MC(T("左图只有一对翅，后面有一对小棒。这是哪一目？", "On the left: one pair of wings and two tiny knobs behind. Which order?", "Di kiri: sepasang sayap dan dua tombol kecil di belakang. Order apa?"),
    [T("膜翅目", "Hymenoptera", "Hymenoptera"), T("双翅目", "Diptera", "Diptera"), T("鳞翅目", "Lepidoptera", "Lepidoptera")], 1,
    T("一对翅加平衡棒是双翅目。", "One pair of wings plus halteres means Diptera.", "Sepasang sayap dan halter bermaksud Diptera."), ["TJ:38"], img="img/svg/key-pairs.svg"),
 TF(T("检索表得出的结果一定正确。", "A key's answer is always right.", "Jawapan kunci sentiasa betul."), False,
    T("检索表只适用于常见昆虫，有例外，要逐项核对。", "Keys cover common insects only and have exceptions; check the features.", "Kunci hanya untuk serangga biasa dan ada pengecualian; semak cirinya."), ["TJ:40"]),
]

write_chapter(chapter, terms, src(*S), quiz)
