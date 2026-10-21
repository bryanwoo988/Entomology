"""p63 — Stage 6: in the field, safely."""
import sys
sys.path.insert(0, 'tools/content')
from build import T, P, L, N, MC, TF, write_chapter
from sources import src

S = ["OSU-COLLECT", "UIDAHO-TIPS", "MSU-4H", "VT-STING", "POISON-CAT", "MJM-1993", "APHC-PAED", "TJ", "URMC-STING"]
chapter = {"id": "p63", "num": 63, "stage": 6, "kind": "lesson",
 "title": T("安全地在野外观察", "Watching insects safely", "Memerhati serangga dengan selamat"),
 "blurb": T("带什么、记什么，以及刺蛾、隐翅虫、蜂类的处理方法", "What to take, what to write down, and what to do about nettle caterpillars, rove beetles, bees and wasps", "Apa yang dibawa, apa yang dicatat, dan apa yang perlu dibuat tentang ulat api, kumbang rove, lebah dan tebuan"),
 "sources": S,
 "sections": [
 {"id": "s1", "heading": T("出发前", "Before you go", "Sebelum keluar"), "level": "basic", "blocks": [
  L(("一个结实的布袋，装工具和标本", "A strong cloth bag to carry your kit and specimens", "Beg kain yang kuat untuk membawa peralatan dan spesimen"),
    ("捕虫网，以及大小不同的小瓶、塑料袋和透明容器", "An insect net, and vials of assorted sizes, plastic bags and clear containers", "Jaring serangga, serta botol kecil pelbagai saiz, beg plastik dan bekas lutsinar"),
    ("拍很小的虫（针头大小或更小）时，放大镜很有用", "A hand lens helps when photographing very small insects, pinhead-sized or smaller", "Kanta pembesar membantu semasa mengambil gambar serangga yang sangat kecil, sebesar kepala pin atau lebih kecil"),
    src=["OSU-COLLECT", "UIDAHO-TIPS"]),
  P("到别人的土地上采集之前，先取得许可。", "Get permission before collecting on someone else's land.", "Dapatkan kebenaran sebelum mengumpul di tanah orang lain.", src=["OSU-COLLECT"])]},
 {"id": "s2", "heading": T("记录观察", "Recording what you see", "Merekod pemerhatian"), "level": "basic", "blocks": [
  P("每次观察或采集，都记下这些资料；之后写标签、查资料都靠它：", "For every observation or sample, write down these details; labels and later checks depend on them:", "Bagi setiap pemerhatian atau sampel, catat butiran ini; label dan semakan kemudian bergantung padanya:", src=["MSU-4H"]),
  L(("日期", "Date", "Tarikh"), ("地点", "Place", "Lokasi"), ("生境（例如稻田、油棕园、树林边）", "Habitat (for example a rice field, an oil palm block, a forest edge)", "Habitat (contohnya sawah, blok sawit, pinggir hutan)"),
    ("天气", "Weather", "Cuaca"), ("用什么方法采到或看到", "How it was collected or seen", "Cara ia dikumpul atau dilihat"), ("记录人", "Who recorded it", "Siapa yang merekod"), src=["MSU-4H"])]},
 {"id": "s3", "heading": T("要小心的虫", "Insects to handle with care", "Serangga yang perlu dikendalikan dengan berhati-hati"), "level": "basic", "blocks": [
  N("warn", "{{ch:p30|刺蛾幼虫}}的刺毛带毒。被螫后，用胶带粘掉断刺，每次换新的一段，再用肥皂和水轻轻清洗。起了很多水泡的话，要去看医生。",
    "{{ch:p30|Nettle caterpillar}} spines carry venom. After a sting, lift the spines out with tape, using a fresh strip each time, then wash gently with soap and water. If the skin blisters badly, see a doctor.",
    "Duri {{ch:p30|ulat api}} berbisa. Selepas disengat, angkat duri dengan pita pelekat, gunakan helaian baharu setiap kali, kemudian basuh perlahan dengan sabun dan air. Jika kulit melepuh teruk, jumpa doktor.",
    src=["VT-STING", "POISON-CAT"]),
  N("warn", "隐翅虫（Paederus）的体液会让皮肤起水泡。不要把它拍死在皮肤上；用别的东西把它拨走，不要用手。万一压碎在皮肤上，要马上用肥皂和水清洗。",
    "The body fluid of Paederus rove beetles blisters the skin. Do not crush one against your skin; brush it off with something other than your hand. If one is smeared on the skin, wash at once with soap and water.",
    "Cecair badan kumbang rove Paederus menyebabkan kulit melepuh. Jangan hancurkannya pada kulit; tepis dengan sesuatu selain tangan. Jika ia tersapu pada kulit, basuh segera dengan sabun dan air.",
    src=["TJ:172", "APHC-PAED", "MJM-1993"]),
  N("warn", "被蜜蜂螫后，用指甲或卡片边缘把螫针刮掉，不要用镊子夹，以免挤进更多毒液。出现呼吸困难或喘鸣、脸部口腔或喉咙肿胀、突然无力、失去知觉，要立刻打紧急电话；医生开过肾上腺素自动注射器的人，马上使用。",
    "After a bee sting, scrape the stinger out with a fingernail or the edge of a card; do not use tweezers, which squeeze in more venom. Call the emergency number at once for wheezing or difficulty breathing, swelling of the face, mouth or throat, sudden weakness or loss of consciousness; anyone prescribed an adrenaline auto-injector should use it straight away.",
    "Selepas disengat lebah, kikis sengat dengan kuku atau tepi kad; jangan guna penyepit, yang memicit lebih banyak bisa masuk. Hubungi nombor kecemasan segera jika berdehit atau sukar bernafas, muka, mulut atau tekak bengkak, tiba-tiba lemah atau tidak sedarkan diri; sesiapa yang diberi suntikan auto adrenalina oleh doktor patut menggunakannya serta-merta.",
    src=["URMC-STING"])]},
 ]}

quiz = [
 MC(T("被刺蛾幼虫螫后，第一步怎样处理断刺？", "After a nettle caterpillar sting, how do you remove the spines?", "Selepas disengat ulat api, bagaimana membuang duri?"),
    [T("用胶带粘掉，每次换新的一段", "Lift them out with tape, a fresh strip each time", "Angkat dengan pita pelekat, helaian baharu setiap kali"), T("用力搓揉", "Rub hard", "Gosok kuat-kuat")], 0,
    T("之后再用肥皂和水清洗。", "Then wash with soap and water.", "Kemudian basuh dengan sabun dan air."), ["VT-STING"]),
 TF(T("隐翅虫停在手臂上，应该一掌拍死它。", "If a rove beetle lands on your arm, slap it.", "Jika kumbang rove hinggap di lengan, tamparnya."), False,
    T("压碎它会让毒液留在皮肤上；用别的东西拨走。", "Crushing it leaves the toxin on your skin; brush it off with something else.", "Menghancurkannya meninggalkan toksin pada kulit; tepis dengan benda lain."), ["APHC-PAED"]),
 MC(T("怎样取出蜜蜂的螫针？", "How should a bee stinger be removed?", "Bagaimana sengat lebah patut dibuang?"),
    [T("用指甲或卡片边缘刮掉", "Scrape it out with a fingernail or card edge", "Kikis dengan kuku atau tepi kad"), T("用镊子夹出来", "Pull it with tweezers", "Tarik dengan penyepit")], 0,
    T("镊子会挤进更多毒液。", "Tweezers squeeze in more venom.", "Penyepit memicit lebih banyak bisa masuk."), ["URMC-STING"]),
 MC(T("记录观察时，哪一项不在建议的清单里？", "Which is not on the suggested recording list?", "Yang manakah tiada dalam senarai rekod yang dicadangkan?"),
    [T("虫的价钱", "The insect's price", "Harga serangga"), T("日期", "Date", "Tarikh"), T("生境", "Habitat", "Habitat")], 0,
    T("要记日期、地点、生境、天气、方法和记录人。", "Record date, place, habitat, weather, method and recorder.", "Rekod tarikh, lokasi, habitat, cuaca, kaedah dan perekod."), ["MSU-4H"]),
]

write_chapter(chapter, [], src(*S), quiz)
