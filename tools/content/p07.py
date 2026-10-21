"""p07 — Classification and scientific names."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, T2, P, L, N, MC, TF, MATCH, write_chapter
from sources import src

S = ["TJ", "ICZN"]
R = lambda *c: [T(*x) for x in c]
chapter = {"id": "p07", "num": 7, "stage": 2, "kind": "lesson",
 "title": T("分类与学名", "Classification and scientific names", "Pengelasan dan nama saintifik"),
 "blurb": T("界门纲目科属种，以及怎样读一个学名", "Kingdom to species, and how to read a scientific name", "Daripada alam hingga spesies, dan cara membaca nama saintifik"),
 "sources": S,
 "sections": [
 {"id": "s1", "heading": T("七个基本阶层", "Seven basic ranks", "Tujuh peringkat asas"), "level": "basic", "blocks": [
  P("生物分类有七个基本阶层：界、门、纲、目、科、属、种。昆虫属于动物界、节肢动物门、昆虫纲。昆虫纲下面再分成许多{{t:order}}，这个 App 主要就是帮你辨识到目。",
    "Living things are classified in seven basic ranks: kingdom, phylum, class, order, family, genus and species. Insects belong to the animal kingdom, the phylum Arthropoda and the class Insecta. The class is split into {{t:order|orders}}, and this app mainly helps you identify an insect to its order.",
    "Benda hidup dikelaskan dalam tujuh peringkat asas: alam, filum, kelas, order, famili, genus dan spesies. Serangga tergolong dalam alam haiwan, filum Arthropoda dan kelas Insecta. Kelas itu dibahagikan kepada banyak {{t:order}}, dan aplikasi ini terutamanya membantu anda mengecam serangga hingga ordernya.",
    defines=["order"], src=["TJ:22"]),
  {"type": "table", "src": ["TJ:22", "TJ:148"],
   "caption": T2("例子：狭臀瓢虫", "例子：波纹瓢虫", "Example: the transverse ladybird", "Contoh: kumbang kura-kura melintang"),
   "headers": R(("阶层", "Rank", "Peringkat"), ("名称", "Name", "Nama")),
   "rows": [R(("界", "Kingdom", "Alam"), ("动物界 Animalia", "Animalia", "Animalia")),
            R(("门", "Phylum", "Filum"), ("节肢动物门 Arthropoda", "Arthropoda", "Arthropoda")),
            R(("纲", "Class", "Kelas"), ("昆虫纲 Insecta", "Insecta", "Insecta")),
            R(("目", "Order", "Order"), ("鞘翅目 Coleoptera", "Coleoptera", "Coleoptera")),
            R(("科", "Family", "Famili"), ("瓢虫科 Coccinellidae", "Coccinellidae", "Coccinellidae")),
            R(("属", "Genus", "Genus"), ("Coccinella", "Coccinella", "Coccinella")),
            R(("种", "Species", "Spesies"), ("Coccinella transversalis", "Coccinella transversalis", "Coccinella transversalis"))]},
  {"type": "gallery", "ids": ["coccinella-transversalis-adult"]},
 ]},
 {"id": "s2", "heading": T("怎样读学名", "Reading a scientific name", "Membaca nama saintifik"), "level": "basic", "blocks": [
  P("每个物种都有一个由两个词组成的{{t:binomial-name}}：第一个是属名，首字母大写；第二个是种小名，全部小写。学名用斜体书写。",
    "Every species has a two-word {{t:binomial-name}}: the genus name, with a capital letter, then the species name, all lower case. Scientific names are written in italics.",
    "Setiap spesies mempunyai {{t:binomial-name}} dua perkataan: nama genus dengan huruf besar, kemudian nama spesies dengan huruf kecil. Nama saintifik ditulis dalam huruf condong.",
    defines=["binomial-name"], src=["ICZN:5.1"]),
  P("学名后面常跟着命名者和年份，例如 Coccinella transversalis Fabricius, 1781。如果命名者和年份放在括号里，表示这个物种后来被移到了另一个属：六斑月瓢虫最初被放在 Coccinella，现在写作 Cheilomenes sexmaculata (Fabricius, 1781)。",
    "A name is often followed by its author and year, as in Coccinella transversalis Fabricius, 1781. When the author and year are in brackets, the species has since been moved to another genus: the six-spotted ladybird was first placed in Coccinella and is now written Cheilomenes sexmaculata (Fabricius, 1781).",
    "Nama sering diikuti oleh pengarang dan tahun, seperti Coccinella transversalis Fabricius, 1781. Apabila pengarang dan tahun dalam kurungan, spesies itu telah dipindahkan ke genus lain: kumbang kura-kura enam bintik mula-mula diletakkan dalam Coccinella dan kini ditulis Cheilomenes sexmaculata (Fabricius, 1781).",
    src=["ICZN:51.3", "TJ:146", "TJ:148"]),
  N("key", "中文俗名各地不同，同一种昆虫在大陆和台湾的叫法常常不一样（例如蝽和椿象）。学名是全世界共用的，查资料时最可靠。",
    "Common names vary from place to place; the same insect often has different Chinese names in mainland China and Taiwan (for example 蝽 and 椿象). A scientific name is shared worldwide, so it is the safest way to look an insect up.",
    "Nama biasa berbeza mengikut tempat; serangga yang sama sering mempunyai nama Cina yang berlainan di China dan Taiwan. Nama saintifik dikongsi di seluruh dunia, jadi ia cara paling selamat untuk mencari maklumat.",
    src=["ICZN:5.1"]),
 ]},
]}

terms = [
 ("order", T("目", "Order", "Order"), T("纲以下、科以上的分类阶层，例如鞘翅目、鳞翅目。", "The rank below class and above family, such as Coleoptera or Lepidoptera.", "Peringkat di bawah kelas dan di atas famili, seperti Coleoptera atau Lepidoptera.")),
 ("binomial-name", T("学名（二名法）", "Scientific name (binomial)", "Nama saintifik (binomial)"), T("由属名和种小名两个词组成的物种名称。", "A species name made of a genus name and a species name.", "Nama spesies yang terdiri daripada nama genus dan nama spesies.")),
]

quiz = [
 MC(T("学名的哪一部分首字母要大写？", "Which part of a scientific name starts with a capital letter?", "Bahagian manakah nama saintifik bermula dengan huruf besar?"), [T("属名", "The genus", "Genus"), T("种小名", "The species name", "Nama spesies"), T("两个都要", "Both", "Kedua-duanya")], 0,
    T("属名首字母大写，种小名全部小写。", "The genus is capitalised; the species name is lower case.", "Genus berhuruf besar; nama spesies berhuruf kecil."), ["ICZN:5.1"]),
 MC(T("昆虫纲属于哪一个门？", "Which phylum does the class Insecta belong to?", "Kelas Insecta tergolong dalam filum mana?"), [T("脊索动物门", "Chordata", "Chordata"), T("节肢动物门", "Arthropoda", "Arthropoda"), T("软体动物门", "Mollusca", "Mollusca")], 1,
    T("昆虫属于节肢动物门。", "Insects are in the phylum Arthropoda.", "Serangga tergolong dalam filum Arthropoda."), ["TJ:22"]),
 TF(T("命名者和年份放在括号里，表示这个物种后来被移到另一个属。", "Brackets around the author and year mean the species has been moved to another genus.", "Kurungan pada pengarang dan tahun bermaksud spesies itu telah dipindahkan ke genus lain."), True,
    T("这是动物命名法规的规定。", "That is the rule in the zoological code.", "Itulah peraturan dalam kod zoologi."), ["ICZN:51.3"]),
 MATCH(T("把阶层和例子配对。", "Match the rank to the example.", "Padankan peringkat dengan contoh."),
    [(T("纲", "Class", "Kelas"), T("昆虫纲", "Insecta", "Insecta")), (T("目", "Order", "Order"), T("鞘翅目", "Coleoptera", "Coleoptera")), (T("科", "Family", "Famili"), T("瓢虫科", "Coccinellidae", "Coccinellidae"))],
    T("昆虫纲是纲，鞘翅目是目，瓢虫科是科。", "Insecta is a class, Coleoptera an order, Coccinellidae a family.", "Insecta ialah kelas, Coleoptera order, Coccinellidae famili."), ["TJ:22"]),
]

write_chapter(chapter, terms, src(*S), quiz)
