"""Stage 5 — fruit: overview (p51) and its insects (p52–p55)."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, MC, TF, CONTROL
from species import species_page, overview_page

STAR = T("杨桃", "Starfruit", "Belimbing")
FRUIT = T("果树", "Fruit trees", "Pokok buah")
CITRUS = T("柑橘类", "Citrus", "Limau")
BANANA = T("香蕉", "Banana", "Pisang")
DAMAGE = T("危害", "Damage", "Kerosakan")

# ---------------------------------------------------------------- p51 overview
overview_page(51, T("果树的昆虫", "Fruit tree insects", "Serangga pokok buah"),
 T("实蝇、柑橘木虱、香蕉弄蝶和柑橘凤蝶", "Fruit flies, the citrus psyllid, the banana skipper and the lime butterfly", "Lalat buah, psilid limau, rama-rama pisang dan rama-rama limau"),
 [L(("{{ch:p52|实蝇}}：杨桃实蝇和橘小实蝇，外形非常像", "{{ch:p52|Fruit flies}}: the carambola fruit fly and the oriental fruit fly, which look very alike", "{{ch:p52|Lalat buah}}: lalat buah belimbing dan lalat buah oriental, yang sangat serupa"),
    ("{{ch:p53|柑橘木虱}}：传播黄龙病，马来西亚最严重的柑橘病害", "{{ch:p53|Asian citrus psyllid}}: spreads huanglongbing, the most serious citrus disease in Malaysia", "{{ch:p53|Psilid limau Asia}}: menyebarkan huanglongbing, penyakit limau paling serius di Malaysia"),
    ("{{ch:p54|香蕉弄蝶}}：幼虫把香蕉叶卷起来吃", "{{ch:p54|Banana skipper}}: its caterpillars roll banana leaves and eat them", "{{ch:p54|Rama-rama pisang}}: ulatnya menggulung daun pisang dan memakannya"),
    ("{{ch:p55|柑橘凤蝶}}：幼虫吃柑橘叶，小时候像鸟粪", "{{ch:p55|Lime butterfly}}: its caterpillars eat citrus leaves, and look like bird droppings when young", "{{ch:p55|Rama-rama limau}}: ulatnya memakan daun limau, dan menyerupai najis burung semasa muda"),
    src=["FFID-CARAM", "PMC-HLB", "PHA-BSK", "UF-PD"]),
  N("key", "实蝇只看外形很难分到种：杨桃实蝇和橘小实蝇外形和基因都很接近，可靠的鉴定需要专家，有时还要用 DNA。",
    "Fruit flies are hard to name to species by eye: the carambola and oriental fruit flies are very close in both form and genes, and a reliable identification needs an expert, sometimes with DNA.",
    "Lalat buah sukar dinamakan hingga spesies dengan mata: lalat buah belimbing dan oriental sangat hampir dari segi rupa dan gen, dan pengecaman yang boleh dipercayai memerlukan pakar, kadang-kadang dengan DNA.",
    src=["IPPC-DP29"])],
 [MC(T("柑橘木虱传播哪一种病？", "Which disease does the Asian citrus psyllid spread?", "Penyakit apakah disebarkan psilid limau Asia?"), [T("黄龙病", "Huanglongbing (citrus greening)", "Huanglongbing (penghijauan limau)"), T("东格鲁病", "Tungro", "Tungro"), T("煤污病", "Sooty mould", "Kulapuk jelaga")], 0,
     T("黄龙病是马来西亚最严重的柑橘病害。", "It is the most serious citrus disease in Malaysia.", "Ia penyakit limau paling serius di Malaysia."), ["PMC-HLB"]),
  TF(T("杨桃实蝇和橘小实蝇用肉眼就能轻易分清。", "Carambola and oriental fruit flies are easy to tell apart by eye.", "Lalat buah belimbing dan oriental mudah dibezakan dengan mata."), False,
     T("两者非常接近，需要专家。", "They are very close; an expert is needed.", "Kedua-duanya sangat hampir; pakar diperlukan."), ["IPPC-DP29"]),
  MC(T("哪一种幼虫小时候像鸟粪？", "Which caterpillar looks like a bird dropping when young?", "Ulat manakah menyerupai najis burung semasa muda?"), [T("柑橘凤蝶", "Lime butterfly", "Rama-rama limau"), T("香蕉弄蝶", "Banana skipper", "Rama-rama pisang")], 0,
     T("最后一龄才变成绿色。", "It turns green only in the last stage.", "Ia menjadi hijau hanya pada peringkat terakhir."), ["UF-PD"])])

# ---------------------------------------------------------------- p52 fruit flies
species_page(52, "fruit-fly", T("实蝇（Bactrocera）", "Fruit flies (carambola and oriental)", "Lalat buah (belimbing dan oriental)"),
 "Bactrocera carambolae, Bactrocera dorsalis", "p14", [STAR, FRUIT], T("成虫", "Adult", "Dewasa"),
 T("幼虫在果实里吃的实蝇，两种非常相似。", "Fruit flies whose maggots feed inside fruit; the two species are very alike.", "Lalat buah yang berenganya makan di dalam buah; dua spesies ini sangat serupa."),
 [("杨桃实蝇：胸部背面暗黑色，小盾片黄色", "Carambola fruit fly: the top of the thorax is dull black and the scutellum (the shield behind it) is yellow", "Lalat buah belimbing: bahagian atas toraks hitam kusam dan skutelum (perisai di belakangnya) kuning"),
  ("胸部两侧各有一条宽的黄色纵带，中间没有黄带", "Two broad yellow stripes run along the sides of the thorax, with no middle stripe", "Dua jalur kuning lebar di sisi toraks, tanpa jalur tengah"),
  ("翅前缘有一条窄的深色带，到翅尖变宽", "A narrow dark band along the front edge of the wing widens at the tip", "Jalur gelap sempit di tepi hadapan sayap melebar di hujung")],
 ["FFID-CARAM"],
 DAMAGE,
 [P("实蝇是杨桃出口必须管理的害虫：马来西亚农业局 2004 年为杨桃出口写的市场准入技术文件，有专门一节讲实蝇的管理。",
    "Fruit flies are a pest that starfruit exports must manage: the Department of Agriculture's 2004 market-access document for exporting starfruit has a section on managing them.",
    "Lalat buah ialah perosak yang mesti diurus untuk eksport belimbing: dokumen teknikal akses pasaran Jabatan Pertanian 2004 untuk eksport belimbing mempunyai bahagian tentang pengurusannya.",
    src=["DOA-CARAM"])],
 lookalike=[
  {"type": "table", "src": ["FFID-CARAM", "FFID-DORS"], "caption": T("杨桃实蝇和橘小实蝇", "Carambola and oriental fruit flies", "Lalat buah belimbing dan oriental"),
   "headers": [T("比较", "Compare", "Banding"), T("杨桃实蝇", "Carambola fruit fly", "Lalat buah belimbing"), T("橘小实蝇", "Oriental fruit fly", "Lalat buah oriental")],
   "rows": [[T("翅尖的深色带", "Dark band at the wing tip", "Jalur gelap di hujung sayap"), T("变宽", "Widens", "Melebar"), T("很窄", "Stays very narrow", "Kekal sangat sempit")],
            [T("腹部第 4–5 节前角的黑斑", "Dark front corners of abdominal segments 4–5", "Sudut hadapan gelap ruas abdomen 4–5"), T("长方形", "Rectangular", "Segi empat tepat"), T("三角形", "Triangular", "Segi tiga")],
            [T("脸上的黑斑", "Face spots", "Bintik muka"), T("椭圆形", "Oval", "Bujur"), T("圆形", "Round", "Bulat")]]},
  N("tip", "两者外形和基因都很接近，诱捕到的虫最好做基因确认。看不准时，交给农业局或专家。",
    "The two are very close in form and genes, so trapped flies are best confirmed genetically. When unsure, send them to the Department of Agriculture or an expert.",
    "Kedua-duanya sangat hampir dari segi rupa dan gen, jadi lalat yang diperangkap sebaiknya disahkan secara genetik. Jika tidak pasti, hantar ke Jabatan Pertanian atau pakar.",
    src=["IPPC-DP29"])],
 controls=[
  CONTROL("monitor", "橘小实蝇的雄虫被甲基丁香酚吸引，可用诱捕器监测；但只靠诱剂不能断定种类。",
    "Oriental fruit fly males are drawn to methyl eugenol, so traps can be used to monitor them; lures alone do not prove the species, though.",
    "Lalat buah oriental jantan tertarik kepada metil eugenol, jadi perangkap boleh digunakan untuk memantaunya; namun pemikat sahaja tidak membuktikan spesies.",
    ["FFID-LURE"]),
  CONTROL("cultural", "出口杨桃要依照农业局市场准入文件里的实蝇管理规定。", "For export starfruit, follow the fruit fly management rules in the Department of Agriculture's market-access document.", "Untuk belimbing eksport, ikut peraturan pengurusan lalat buah dalam dokumen akses pasaran Jabatan Pertanian.", ["DOA-CARAM"])],
 photos=["bactrocera-carambolae-adult", "bactrocera-dorsalis-adult"],
 quiz=[MC(T("杨桃实蝇翅尖的深色带是怎样的？", "What does the dark band at the carambola fruit fly's wing tip do?", "Bagaimanakah jalur gelap di hujung sayap lalat buah belimbing?"), [T("变宽", "It widens", "Ia melebar"), T("消失", "It disappears", "Ia hilang"), T("变成红色", "It turns red", "Ia menjadi merah")], 0,
          T("橘小实蝇的则保持很窄。", "In the oriental fruit fly it stays very narrow.", "Pada lalat buah oriental ia kekal sangat sempit."), ["FFID-CARAM", "FFID-DORS"]),
       MC(T("橘小实蝇的雄虫被什么吸引？", "What attracts oriental fruit fly males?", "Apakah yang menarik lalat buah oriental jantan?"), [T("甲基丁香酚", "Methyl eugenol", "Metil eugenol"), T("Cue-lure", "Cue-lure", "Cue-lure")], 0,
          T("Cue-lure 吸引的是瓜实蝇。", "Cue-lure attracts the melon fly.", "Cue-lure menarik lalat buah tembikai."), ["FFID-LURE"]),
       TF(T("杨桃实蝇胸部中央有一条黄色纵带。", "The carambola fruit fly has a yellow stripe down the middle of the thorax.", "Lalat buah belimbing mempunyai jalur kuning di tengah toraks."), False,
          T("它只有两侧的黄带，中间没有。", "It has only the side stripes, none in the middle.", "Ia hanya mempunyai jalur sisi, tiada di tengah."), ["FFID-CARAM"])])

# ---------------------------------------------------------------- p53 Asian citrus psyllid
species_page(53, "citrus-psyllid", T("柑橘木虱（Diaphorina citri）", "Asian citrus psyllid", "Psilid limau Asia"),
 "Diaphorina citri", "p12", [CITRUS], T("若虫和成虫", "Nymphs and adults", "Nimfa dan dewasa"),
 T("传播柑橘黄龙病的小型木虱。", "A small psyllid that spreads citrus huanglongbing.", "Psilid kecil yang menyebarkan huanglongbing limau."),
 [("吸食时身体和叶面约成 45 度：头低贴叶，腹部翘起", "When feeding, it holds its body at about 45° to the leaf, head down and abdomen raised", "Semasa makan, badannya kira-kira 45° dari daun, kepala ke bawah dan abdomen terangkat"),
  ("若虫从尾部分泌卷曲、末端成球状的蜡管，用来排走蜜露；这种蜡管是它独有的", "Each nymph makes a curly waxy tube with a bulb at the end to carry its honeydew away; this tube is unique to it", "Setiap nimfa membuat tiub lilin berpintal dengan bebola di hujung untuk membuang embun madunya; tiub ini unik kepadanya")],
 ["DPIRD-ACP", "UC-ACP"],
 DAMAGE,
 [P("它传播 'Candidatus Liberibacter asiaticus'，即亚洲型黄龙病（柑橘绿化病）的病原，这是马来西亚最严重的柑橘病害。",
    "It spreads 'Candidatus Liberibacter asiaticus', the cause of the severe Asian form of huanglongbing (citrus greening), the most serious citrus disease in Malaysia.",
    "Ia menyebarkan 'Candidatus Liberibacter asiaticus', punca bentuk Asia huanglongbing (penghijauan limau) yang teruk, penyakit limau paling serius di Malaysia.",
    src=["PMC-HLB"]),
  P("黄龙病在马来西亚扩散，主要是因为广泛使用带病的圈枝（高压）苗，加上田间发现得慢。",
    "Its spread in Malaysia was helped mainly by the wide use of infected air-layered planting material, and by slow detection in the field.",
    "Penularannya di Malaysia dibantu terutamanya oleh penggunaan meluas anak benih tut yang dijangkiti, dan pengesanan yang lambat di ladang.",
    src=["FFTC-HLB"])],
 controls=[
  CONTROL("cultural", "种无病种苗，砍除染病的树。", "Plant disease-free planting material and remove infected trees.", "Tanam bahan tanaman bebas penyakit dan buang pokok yang dijangkiti.", ["PMC-HLB", "FFTC-HLB"]),
  CONTROL("biological", "寄生蜂 Tamarixia radiata 寄生木虱若虫。不过在巴西和美国，许多果农认为单靠天敌不足以减缓黄龙病的扩散。",
    "The wasp Tamarixia radiata parasitises the psyllid's nymphs. In Brazil and the USA, though, many growers consider natural enemies alone not enough to slow the spread of huanglongbing.",
    "Tebuan Tamarixia radiata memparasit nimfa psilid. Namun di Brazil dan Amerika Syarikat, ramai penanam menganggap musuh semula jadi sahaja tidak cukup untuk melambatkan penularan huanglongbing.",
    ["UF-TAMAR", "HALL-2008"]),
  CONTROL("chemical", "砂拉越的综合防治建议是审慎地使用杀虫剂。只用农业局为柑橘登记的产品，并依照标签。",
    "The Sarawak IPM review advises careful (judicious) use of insecticides. Use only products registered by the Department of Agriculture for citrus, and follow the label.",
    "Kajian IPM Sarawak menasihatkan penggunaan racun serangga secara berhemat. Gunakan hanya produk berdaftar Jabatan Pertanian untuk limau, dan ikut label.",
    ["PMC-HLB", "DOA-MRL"])],
 photos=["diaphorina-citri-adult", "diaphorina-citri-nymph"],
 authority="Kuwayama",
 quiz=[MC(T("柑橘木虱吸食时是什么姿势？", "How does the citrus psyllid sit when feeding?", "Bagaimanakah kedudukan psilid limau semasa makan?"), [T("头低尾翘，约 45 度", "Head down, abdomen raised, about 45°", "Kepala ke bawah, abdomen terangkat, kira-kira 45°"), T("平贴在叶上", "Flat on the leaf", "Rata pada daun")], 0,
          T("这个姿势有助野外辨认。", "The posture helps identify it in the field.", "Kedudukan ini membantu pengecaman di lapangan."), ["DPIRD-ACP"]),
       TF(T("用带病的圈枝苗是黄龙病在马来西亚扩散的主要原因之一。", "Infected air-layered planting material helped huanglongbing spread in Malaysia.", "Anak benih tut yang dijangkiti membantu penularan huanglongbing di Malaysia."), True,
          T("所以要用无病种苗。", "So use disease-free planting material.", "Jadi gunakan bahan tanaman bebas penyakit."), ["FFTC-HLB"]),
       MC(T("Tamarixia radiata 是什么？", "What is Tamarixia radiata?", "Apakah Tamarixia radiata?"), [T("寄生木虱若虫的小蜂", "A wasp that parasitises psyllid nymphs", "Tebuan yang memparasit nimfa psilid"), T("一种柑橘品种", "A citrus variety", "Varieti limau")], 0,
          T("它是天敌。", "It is a natural enemy.", "Ia musuh semula jadi."), ["UF-TAMAR"])])

# ---------------------------------------------------------------- p54 banana skipper
species_page(54, "banana-skipper", T("弄蝶（Erionota）", "Banana skipper", "Rama-rama pisang"),
 "Erionota thrax", "p11", [BANANA], T("幼虫", "Larva", "Larva"),
 T("幼虫把香蕉叶卷成筒、躲在里面吃的弄蝶。", "A skipper butterfly whose caterpillars roll banana leaves into tubes and feed inside.", "Rama-rama skipper yang ulatnya menggulung daun pisang menjadi tiub dan makan di dalamnya."),
 [("幼虫头部黑亮，身体淡绿色，盖着白色蜡粉，长可达 6 厘米", "The caterpillar has a shiny black head and a pale green body covered in white waxy powder, up to 6 cm long", "Ulat berkepala hitam berkilat dan berbadan hijau pucat yang ditutup serbuk lilin putih, sehingga 6 cm panjang"),
  ("躲在长达 15 厘米的叶卷里，叶卷内有白色蜡质", "It hides in leaf rolls up to 15 cm long, lined with white wax", "Ia bersembunyi dalam gulungan daun sehingga 15 cm panjang, berlapik lilin putih")],
 ["PHA-BSK"],
 DAMAGE,
 [P("大发生时，可吃掉香蕉多达 60% 的叶面积。", "Outbreaks have destroyed up to 60% of banana leaf area.", "Serangan besar telah memusnahkan sehingga 60% keluasan daun pisang.", src=["PHA-BSK"])],
 lookalike=[P("近缘种 Erionota torus 分布到马来西亚半岛，很容易和 E. thrax 混淆，确认可能要检查雄虫的生殖器。",
    "The related Erionota torus ranges into Peninsular Malaysia and is easily confused with E. thrax; confirming it may require examining the male genitalia.",
    "Spesies berkait Erionota torus terdapat hingga Semenanjung Malaysia dan mudah dikelirukan dengan E. thrax; pengesahan mungkin memerlukan pemeriksaan genitalia jantan.",
    src=["PLAZI-ET"])],
 controls=[
  CONTROL("biological", "关岛、毛里求斯和夏威夷从泰国引进卵寄生蜂 Ooencyrtus erionotae 和幼虫寄生蜂 Cotesia erionotae 后，生物防治成功。在印尼，这两种也是主要的寄生蜂。",
    "Biological control worked in Guam, Mauritius and Hawaii after the egg parasitoid Ooencyrtus erionotae and the larval parasitoid Cotesia erionotae were brought in from Thailand. In Indonesia these two are also among the main parasitoids.",
    "Kawalan biologi berjaya di Guam, Mauritius dan Hawaii selepas parasitoid telur Ooencyrtus erionotae dan parasitoid larva Cotesia erionotae dibawa masuk dari Thailand. Di Indonesia kedua-duanya juga antara parasitoid utama.",
    ["SANDS-BSK", "BIODIV-ET"])],
 photos=["erionota-thrax-larva", "erionota-thrax-adult"],
 authority="(Linnaeus)",
 quiz=[MC(T("香蕉弄蝶的幼虫住在哪里？", "Where does the banana skipper caterpillar live?", "Di manakah ulat rama-rama pisang tinggal?"), [T("卷起来的香蕉叶里", "Inside a rolled banana leaf", "Di dalam daun pisang yang digulung"), T("香蕉果里", "Inside the fruit", "Di dalam buah"), T("土里", "In the soil", "Di dalam tanah")], 0,
          T("叶卷长达 15 厘米。", "The rolls are up to 15 cm long.", "Gulungan sehingga 15 cm panjang."), ["PHA-BSK"]),
       MC(T("幼虫身上盖着什么？", "What covers the caterpillar's body?", "Apakah yang menutupi badan ulat?"), [T("白色蜡粉", "White waxy powder", "Serbuk lilin putih"), T("黑色长毛", "Long black hairs", "Bulu hitam panjang")], 0,
          T("头部则是黑亮的。", "Its head is shiny black.", "Kepalanya hitam berkilat."), ["PHA-BSK"]),
       TF(T("引进寄生蜂曾成功控制香蕉弄蝶。", "Introduced parasitoids have controlled the banana skipper.", "Parasitoid yang dibawa masuk pernah mengawal rama-rama pisang."), True,
          T("关岛、毛里求斯和夏威夷都成功了。", "It worked in Guam, Mauritius and Hawaii.", "Ia berjaya di Guam, Mauritius dan Hawaii."), ["SANDS-BSK"])])

# ---------------------------------------------------------------- p55 lime butterfly
species_page(55, "lime-butterfly", T("凤蝶（Papilio demoleus）", "Lime butterfly", "Rama-rama limau"),
 "Papilio demoleus", "p11", [CITRUS], T("幼虫", "Larva", "Larva"),
 T("幼虫吃柑橘叶的凤蝶。", "A swallowtail whose caterpillars eat citrus leaves.", "Rama-rama ekor walet yang ulatnya memakan daun limau."),
 [("1–4 龄幼虫黑色，前、中、后有宽的灰白色横带，看起来像鸟粪", "Caterpillars in stages 1–4 are black with broad off-white bands at the front, middle and rear, so they look like bird droppings", "Ulat peringkat 1–4 hitam dengan jalur putih kusam lebar di depan, tengah dan belakang, jadi kelihatan seperti najis burung"),
  ("第 5 龄（最后一龄）变成绿色", "The fifth (last) stage turns green", "Peringkat kelima (terakhir) menjadi hijau")],
 ["UF-PD"],
 T("危害", "Damage", "Kerosakan"),
 [P("幼虫吃柑橘类的叶子，是柑橘的害虫。", "The caterpillars eat the leaves of citrus and are a pest of citrus.", "Ulatnya memakan daun limau dan merupakan perosak limau.", src=["UF-PD"])],
 photos=["papilio-demoleus-larva", "papilio-demoleus-adult"],
 authority="Linnaeus",
 quiz=[MC(T("柑橘凤蝶的小幼虫看起来像什么？", "What do young lime butterfly caterpillars look like?", "Ulat muda rama-rama limau kelihatan seperti apa?"), [T("鸟粪", "Bird droppings", "Najis burung"), T("树枝", "Twigs", "Ranting"), T("花", "Flowers", "Bunga")], 0,
          T("黑色加灰白色横带。", "Black with off-white bands.", "Hitam dengan jalur putih kusam."), ["UF-PD"]),
       TF(T("柑橘凤蝶的最后一龄幼虫是绿色的。", "The last-stage lime butterfly caterpillar is green.", "Ulat rama-rama limau peringkat terakhir berwarna hijau."), True,
          T("第 5 龄变绿。", "The fifth stage turns green.", "Peringkat kelima menjadi hijau."), ["UF-PD"]),
       MC(T("柑橘凤蝶的幼虫吃什么？", "What do lime butterfly caterpillars eat?", "Apakah makanan ulat rama-rama limau?"), [T("柑橘叶", "Citrus leaves", "Daun limau"), T("香蕉叶", "Banana leaves", "Daun pisang")], 0,
          T("所以叫柑橘凤蝶。", "Hence its name.", "Itulah sebab namanya."), ["UF-PD"])])
