/* Language resolution and the interface string table.

   Every translatable value is a {zh, en, ms} object; pick() is the single
   place that turns one into a string. Knows nothing about the DOM. */

import { get as getPrefs } from './prefs.js';

const FALLBACK = ['en', 'zh', 'ms'];

// Short name of each language (tests and compact labels).
export const LANG_GLYPH = { zh: '中', en: 'EN', ms: 'BM' };

// Each language named in itself: the first-run picker appears before any
// language has been chosen to label the others in.
export const LANG_NATIVE = { zh: '中文', en: 'English', ms: 'Bahasa Melayu' };

export function current() {
  return getPrefs().lang;
}

export function pick(value, lang = current()) {
  if (value == null) return '';
  if (typeof value === 'string' || typeof value === 'number') return String(value);
  if (value[lang]) return value[lang];
  for (const f of FALLBACK) {
    if (value[f]) {
      // The content linter stops this shipping; in development, make it findable.
      console.warn(`[i18n] missing "${lang}":`, String(value[f]).slice(0, 40));
      return value[f];
    }
  }
  return '';
}

export function t(key, vars, lang = current()) {
  let s = pick(UI[key], lang);
  if (!s) console.warn(`[i18n] no UI string "${key}"`);
  if (vars) for (const [k, v] of Object.entries(vars)) s = s.replaceAll(`{${k}}`, String(v));
  return s;
}

export const UI = {
  appName: { zh: '昆虫', en: 'Bugs', ms: 'Serangga' },
  tagline: {
    zh: '认识昆虫、一步一步辨识到目，以及马来西亚常见的农业昆虫——离线三语',
    en: "Meet the insects, identify them step by step, and learn Malaysia's farm insects — offline, in three languages",
    ms: 'Kenali serangga, kenal pasti langkah demi langkah, dan pelajari serangga pertanian Malaysia — luar talian, dalam tiga bahasa',
  },
  pickTitle: { zh: '选择语言', en: 'Choose your language', ms: 'Pilih bahasa anda' },
  pickHint: { zh: '之后随时可以在底部的「设置」里切换', en: 'You can change it any time in Settings, at the bottom of the screen', ms: 'Anda boleh menukarnya bila-bila masa dalam Tetapan, di bawah skrin' },

  home: { zh: '首页', en: 'Home', ms: 'Utama' },
  stageN: { zh: '阶段 {n}', en: 'Stage {n}', ms: 'Peringkat {n}' },
  chapterN: { zh: '第 {n} 章', en: 'Chapter {n}', ms: 'Bab {n}' },
  chaptersCount: { zh: '{n} 章', en: '{n} chapters', ms: '{n} bab' },
  progress: { zh: '已读 {done}/{total}', en: '{done} of {total} read', ms: '{done}/{total} dibaca' },
  continueReading: { zh: '继续上次阅读', en: 'Continue reading', ms: 'Sambung membaca' },
  startHere: { zh: '从第一章开始', en: 'Start with Chapter 1', ms: 'Mula dengan Bab 1' },
  newTerms: { zh: '本章新名词', en: 'New in this chapter', ms: 'Istilah baharu bab ini' },
  advanced: { zh: '进阶', en: 'Going deeper', ms: 'Lanjutan' },
  farmInsects: { zh: '这一目的农业昆虫', en: 'Farm insects in this order', ms: 'Serangga pertanian dalam order ini' },
  viaSearch: { zh: '（经搜索摘要核对，未能打开原文）', en: '(checked through a search summary; the page itself could not be opened)', ms: '(disemak melalui ringkasan carian; halaman asal tidak dapat dibuka)' },
  sources: { zh: '本章来源', en: 'Sources for this chapter', ms: 'Sumber bab ini' },
  prev: { zh: '上一章', en: 'Previous', ms: 'Sebelumnya' },
  next: { zh: '下一章', en: 'Next', ms: 'Seterusnya' },
  markRead: { zh: '标记为已读', en: 'Mark as read', ms: 'Tanda sudah dibaca' },
  isRead: { zh: '已读', en: 'Read', ms: 'Sudah dibaca' },
  detailIn: { zh: '详见第 {n} 章', en: 'Explained in Chapter {n}', ms: 'Diterangkan dalam Bab {n}' },
  openChapter: { zh: '打开这一章', en: 'Open the chapter', ms: 'Buka bab' },
  close: { zh: '关闭', en: 'Close', ms: 'Tutup' },
  schematic: { zh: '示意图', en: 'Schematic', ms: 'Ilustrasi' },
  source: { zh: '来源', en: 'Source', ms: 'Sumber' },
  needsNet: { zh: '需要网络', en: 'Needs internet', ms: 'Perlu internet' },

  noteTip: { zh: '小提示', en: 'Tip', ms: 'Tip' },
  noteWarn: { zh: '注意', en: 'Caution', ms: 'Awas' },
  noteKey: { zh: '重点', en: 'Key point', ms: 'Perkara utama' },
  noteMyth: { zh: '常见误解', en: 'Common misconception', ms: 'Salah faham biasa' },

  search: { zh: '搜索', en: 'Search', ms: 'Cari' },
  searchHint: { zh: '搜索章节和名词（三种语言都可以）', en: 'Search chapters and terms, in any of the three languages', ms: 'Cari bab dan istilah, dalam mana-mana tiga bahasa' },
  noResults: { zh: '找不到结果', en: 'No results', ms: 'Tiada hasil' },

  tools: { zh: '工具', en: 'Tools', ms: 'Alatan' },
  glossary: { zh: '名词词典', en: 'Glossary', ms: 'Glosari' },
  flashcards: { zh: '名词闪卡', en: 'Flashcards', ms: 'Kad imbas' },
  quiz: { zh: '自测题', en: 'Self-test', ms: 'Uji diri' },

  info: { zh: '关于', en: 'About', ms: 'Perihal' },
  share: { zh: '分享', en: 'Share', ms: 'Kongsi' },
  shareHint: { zh: '扫描二维码，用浏览器直接打开这个 App', en: 'Scan to open the app in a browser', ms: 'Imbas untuk membuka aplikasi dalam pelayar' },
  shareButton: { zh: '分享链接', en: 'Share link', ms: 'Kongsi pautan' },
  copyLink: { zh: '复制链接', en: 'Copy link', ms: 'Salin pautan' },
  copied: { zh: '已复制', en: 'Copied', ms: 'Disalin' },
  createdBy: { zh: 'Apps created by Bryan Woo', en: 'Apps created by Bryan Woo', ms: 'Apps created by Bryan Woo' },
  version: { zh: '版本', en: 'Version', ms: 'Versi' },
  offlineReady: { zh: '已可离线使用', en: 'Ready to use offline', ms: 'Sedia digunakan luar talian' },
  offlineNotYet: { zh: '尚未完成离线下载', en: 'Offline download not finished yet', ms: 'Muat turun luar talian belum selesai' },
  allSources: { zh: '资料来源', en: 'Sources', ms: 'Sumber' },

  updateReady: { zh: '有新版本', en: 'A new version is ready', ms: 'Versi baharu sedia' },
  updateNow: { zh: '立即更新', en: 'Update now', ms: 'Kemas kini sekarang' },
  updatedTo: { zh: '已更新到 v{v}', en: 'Updated to v{v}', ms: 'Dikemas kini ke v{v}' },
  offline: { zh: '离线', en: 'Offline', ms: 'Luar talian' },
  contents: { zh: '目录', en: 'Contents', ms: 'Kandungan' },
  allUpdates: { zh: '更新记录', en: "What's new", ms: 'Apa yang baharu' },
  ok: { zh: '好的', en: 'OK', ms: 'OK' },

  theme: { zh: '外观', en: 'Appearance', ms: 'Paparan' },
  menu: { zh: '菜单', en: 'Menu', ms: 'Menu' },
  readAloud: { zh: '朗读', en: 'Read aloud', ms: 'Baca kuat' },
  stopReading: { zh: '停止', en: 'Stop', ms: 'Henti' },
  settings: { zh: '设置', en: 'Settings', ms: 'Tetapan' },
  language: { zh: '语言', en: 'Language', ms: 'Bahasa' },
  textSize: { zh: '字号', en: 'Text size', ms: 'Saiz teks' },
  textSample: { zh: '瓢虫坚硬的前翅在背上沿着一条直线合拢。', en: "A ladybird's hard forewings meet in a straight line down its back.", ms: 'Sayap depan kumbang kura-kura yang keras bertemu dalam satu garis lurus di belakangnya.' },
  openChapterFirst: { zh: '先打开一章，再按「朗读」', en: 'Open a chapter first, then Read aloud', ms: 'Buka satu bab dahulu, kemudian Baca kuat' },
  notes: { zh: '笔记', en: 'Notes', ms: 'Nota' },
  highlights: { zh: '画线', en: 'Highlights', ms: 'Serlahan' },
  bookmarks: { zh: '书签', en: 'Bookmarks', ms: 'Penanda' },
  markHint: { zh: '点一下段落可以画线、写笔记、加书签或从这里朗读；长按选取几个字，只标记那几个字。', en: 'Tap a paragraph to highlight it, add a note, bookmark it or read aloud from there; long-press to mark just a few words.', ms: 'Ketik perenggan untuk menyerlah, menambah nota, menanda atau membaca kuat dari situ; tekan lama untuk menanda beberapa perkataan sahaja.' },
  themeAuto: { zh: '跟随系统', en: 'Match system', ms: 'Ikut sistem' },
  themeLight: { zh: '浅色', en: 'Light', ms: 'Cerah' },
  themeDark: { zh: '深色', en: 'Dark', ms: 'Gelap' },
  themeNote: { zh: '「跟随系统」时，手机为浅色就用浅色主题，为深色就用深色主题。', en: 'In Match system mode the app follows your phone: your light theme when the phone is light, your dark theme when it is dark.', ms: 'Dalam mod Ikut sistem, apl mengikut telefon anda: tema cerah apabila telefon cerah, tema gelap apabila telefon gelap.' },
  lightLooks: { zh: '浅色主题', en: 'Light theme', ms: 'Tema cerah' },
  darkLooks: { zh: '深色主题', en: 'Dark theme', ms: 'Tema gelap' },
  look_classic: { zh: '经典', en: 'Classic', ms: 'Klasik' },
  look_paper: { zh: '纸张', en: 'Paper', ms: 'Kertas' },
  look_mint: { zh: '薄荷', en: 'Mint', ms: 'Pudina' },
  look_lavender: { zh: '薰衣草', en: 'Lavender', ms: 'Lavender' },
  look_midnight: { zh: '午夜', en: 'Midnight', ms: 'Tengah Malam' },
  look_oled: { zh: '纯黑 OLED', en: 'OLED Black', ms: 'Hitam OLED' },
  look_slate: { zh: '石板', en: 'Slate', ms: 'Batu Loh' },
  look_grape: { zh: '葡萄', en: 'Grape', ms: 'Anggur' },
  more: { zh: '更多', en: 'More', ms: 'Lagi' },
  submit: { zh: '提交', en: 'Submit', ms: 'Hantar' },
  exam: { zh: '考试', en: 'Exam', ms: 'Peperiksaan' },
  examPick: { zh: '选择题数，开始考试。交卷后才显示答案。', en: 'Pick how many questions. Answers are shown after you submit.', ms: 'Pilih bilangan soalan. Jawapan ditunjukkan selepas anda menghantar.' },
  examN: { zh: '{n} 题', en: '{n} questions', ms: '{n} soalan' },
  examTimer: { zh: '计时', en: 'Time me', ms: 'Kira masa' },
  examTime: { zh: '用时 {m} 分 {s} 秒', en: 'Time: {m} min {s} s', ms: 'Masa: {m} min {s} s' },
  examHistory: { zh: '考试记录', en: 'Exam history', ms: 'Sejarah peperiksaan' },
  wrongBook: { zh: '错题本', en: 'Wrong answers', ms: 'Buku salah jawab' },
  wrongEmpty: { zh: '错题本是空的。', en: 'No wrong answers to redo.', ms: 'Tiada jawapan salah untuk diulang.' },
  wrongHint: { zh: '再答一次；答对了就会从错题本移除。', en: 'Try again; a right answer removes the question from this list.', ms: 'Cuba lagi; jawapan betul membuang soalan daripada senarai ini.' },
  progress: { zh: '学习进度', en: 'Progress', ms: 'Kemajuan' },
  stage: { zh: '阶段', en: 'Stage', ms: 'Peringkat' },
  pagesRead: { zh: '已读', en: 'Read', ms: 'Dibaca' },
  bestQuiz: { zh: '小测验最高分', en: 'Best quiz', ms: 'Kuiz terbaik' },
  cardsDue: { zh: '今天还要复习 {n} 张', en: '{n} cards to review today', ms: '{n} kad untuk diulang kaji hari ini' },
  cardsDone: { zh: '今天的闪卡复习完了。', en: "You're done for today.", ms: 'Selesai untuk hari ini.' },
  cardYes: { zh: '记得', en: 'Knew it', ms: 'Ingat' },
  cardNo: { zh: '不记得', en: "Didn't", ms: 'Tak ingat' },
  allStages: { zh: '全部', en: 'All', ms: 'Semua' },
  noQuestions: { zh: '还没有题目。', en: 'No questions yet.', ms: 'Belum ada soalan.' },
  identify: { zh: '辨识', en: 'Identify', ms: 'Kenal pasti' },
  keyIntro: { zh: '一次回答一个问题，辨识到昆虫的目。只适用于成虫。', en: 'Answer one question at a time to find the insect order. For adult insects.', ms: 'Jawab satu soalan pada satu masa untuk mencari order serangga. Untuk serangga dewasa.' },
  keyStep: { zh: '第 {n} 题', en: 'Question {n}', ms: 'Soalan {n}' },
  keyCantTell: { zh: '看不清楚？', en: "Can't tell?", ms: 'Tidak pasti?' },
  keyResult: { zh: '结果', en: 'Result', ms: 'Keputusan' },
  keyCheck: { zh: '逐项核对', en: 'Check each feature', ms: 'Semak setiap ciri' },
  keyConfused: { zh: '容易混淆', en: 'Easily confused with', ms: 'Mudah dikelirukan dengan' },
  keyDisclaimer: { zh: '只适用于常见昆虫的成虫，精确鉴定请教专家。', en: 'For adults of common insects only; ask an expert for a firm identification.', ms: 'Untuk serangga dewasa yang biasa sahaja; rujuk pakar untuk pengecaman yang pasti.' },
  keyRestart: { zh: '重新开始', en: 'Start again', ms: 'Mula semula' },
  openOrder: { zh: '查看这个目', en: 'Read about this order', ms: 'Baca tentang order ini' },
  orderLabel: { zh: '所属目', en: 'Order', ms: 'Order' },
  cropsLabel: { zh: '作物', en: 'Crops', ms: 'Tanaman' },
  damagingStage: { zh: '造成危害的虫期', en: 'Damaging stage', ms: 'Peringkat yang merosakkan' },
  activeIngredients: { zh: '有效成分', en: 'Active ingredients', ms: 'Bahan aktif' },
  ipm_monitor: { zh: '监测', en: 'Monitoring', ms: 'Pemantauan' },
  ipm_cultural: { zh: '栽培与物理防治', en: 'Cultural and physical control', ms: 'Kawalan kultur dan fizikal' },
  ipm_biological: { zh: '生物防治', en: 'Biological control', ms: 'Kawalan biologi' },
  ipm_chemical: { zh: '化学防治', en: 'Chemical control', ms: 'Kawalan kimia' },
  pesticideWarning: { zh: '使用任何农药前，请阅读并遵守标签说明，并以农业部（DOA）与农药局的最新指引为准。', en: 'Before using any pesticide, read and follow its label, and check the latest guidance from the Department of Agriculture (DOA) and the Pesticides Board.', ms: 'Sebelum menggunakan sebarang racun perosak, baca dan patuhi labelnya, dan rujuk panduan terkini Jabatan Pertanian (DOA) dan Lembaga Racun Makhluk Perosak.' },
  noPhoto: { zh: '暂无照片', en: 'No photo yet', ms: 'Tiada foto lagi' },
  photoCredits: { zh: '图片来源', en: 'Photo credits', ms: 'Kredit foto' },
  loading: { zh: '载入中…', en: 'Loading…', ms: 'Memuatkan…' },
  loadError: { zh: '内容载入失败', en: 'Could not load this page', ms: 'Gagal memuatkan halaman ini' },
};
