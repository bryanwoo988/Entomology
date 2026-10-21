/* Flashcard scheduling with five Leitner boxes. A right answer moves a card
   up a box and pushes its next review further out; a wrong one sends it back
   to box 1 for today. Dates are local YYYY-MM-DD strings. Pure. */

export const BOXES = 5;
export const INTERVAL_DAYS = [0, 1, 3, 7, 14];

export function addDays(day, n) {
  const d = new Date(`${day}T00:00:00Z`);
  d.setUTCDate(d.getUTCDate() + n);
  return d.toISOString().slice(0, 10);
}

export function review(state, cardId, correct, today) {
  const box = correct ? Math.min(BOXES, (state[cardId]?.box ?? 1) + 1) : 1;
  return { ...state, [cardId]: { box, due: addDays(today, INTERVAL_DAYS[box - 1]) } };
}

// Unseen cards count as box 1, due now.
export function dueCards(state, cardIds, today) {
  return cardIds
    .map((id, i) => ({ id, i, box: state[id]?.box ?? 0, due: state[id]?.due ?? '' }))
    .filter(c => !c.due || c.due <= today)
    .sort((a, b) => a.box - b.box || a.due.localeCompare(b.due) || a.i - b.i)
    .map(c => c.id);
}
