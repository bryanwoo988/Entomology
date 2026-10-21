/* The identification key: a tree of questions, each option leading to the
   next question or to a result. A walk is the list of chosen option indexes,
   which is also what the URL carries (#/key/0.1.1). Pure. */

export function walk(key, answers) {
  const path = [];
  let node = key.start;
  for (const choice of answers) {
    const opt = key.nodes[node]?.options?.[choice];
    if (!opt) break;
    path.push({ node, choice });
    if (opt.result) return { path, result: opt.result };
    node = opt.next;
  }
  return { path, node };
}

// Answer question `step` again: everything after it is dropped.
export const answerAt = (answers, step, choice) => answers.slice(0, step).concat(choice);

export const encode = answers => answers.join('.');

export function decode(str) {
  const s = String(str ?? '');
  return /^\d+(\.\d+)*$/.test(s) ? s.split('.').map(Number) : [];
}

export function validate(key) {
  const errors = [];
  if (!key.nodes?.[key.start]) errors.push(`start "${key.start}" is not a question`);
  for (const [id, n] of Object.entries(key.nodes ?? {})) {
    (n.options ?? []).forEach((o, i) => {
      if (!!o.next === !!o.result) errors.push(`${id} option ${i}: needs exactly one of next/result`);
      if (o.next && !key.nodes[o.next]) errors.push(`${id} option ${i}: unknown question "${o.next}"`);
      if (o.result && !key.results?.[o.result]) errors.push(`${id} option ${i}: unknown result "${o.result}"`);
    });
  }
  // Depth-first from the start: a node met again on the current path is a cycle.
  const seen = new Set(), onPath = new Set();
  const visit = id => {
    if (onPath.has(id)) { errors.push(`cycle through "${id}"`); return; }
    if (seen.has(id) || !key.nodes[id]) return;
    seen.add(id); onPath.add(id);
    for (const o of key.nodes[id].options ?? []) if (o.next) visit(o.next);
    onPath.delete(id);
  };
  visit(key.start);
  for (const id of Object.keys(key.nodes ?? {})) if (!seen.has(id)) errors.push(`${id} is unreachable`);
  return errors;
}
