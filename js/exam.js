/* Exams: drawing questions and marking answers. Pure.

   Item types (data/quiz.json):
     mc     {q, options[2..4], answer}         — true/false is mc with two options
     match  {q, pairs[{left, right}] (3..5)}   — answered as response[i] = chosen right index for pairs[i]
   An item without `type` is mc. */

export const kindOf = item => item.type ?? 'mc';

// Stable across sessions and languages: page plus the English question.
export function itemId(item) {
  const s = `${item.chapter}|${item.q?.en ?? ''}`;
  let h = 5381;
  for (let i = 0; i < s.length; i++) h = ((h * 33) ^ s.charCodeAt(i)) >>> 0;
  return `${item.chapter}-${h.toString(36)}`;
}

// Small seeded generator (mulberry32) so an exam can be redrawn exactly.
function rng(seed) {
  let a = seed >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

export function drawExam(items, { count, stages, seed = 1 }) {
  const pool = items.filter(q => !stages?.length || stages.includes(q.stage));
  const rand = rng(seed), a = [...pool];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(rand() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a.slice(0, Math.min(count, a.length));
}

export function scoreItem(item, response) {
  if (kindOf(item) === 'match') {
    return Array.isArray(response) && response.length === item.pairs.length && response.every((r, i) => r === i);
  }
  return response === item.answer;
}

export function scoreExam(items, responses) {
  const wrongIds = [];
  let correct = 0;
  items.forEach((q, i) => { if (scoreItem(q, responses[i])) correct++; else wrongIds.push(itemId(q)); });
  return { correct, total: items.length, wrongIds };
}
