/**
 * Returns a string expressing preference for const.
 * @returns {string} A constant string.
 */
export function taskFirst() {
  const task = 'I prefer const when I can.';
  return task;
}

/**
 * Returns a string to be appended.
 * @returns {string} A constant string.
 */
export function getLast() {
  return ' is okay';
}

/**
 * Combines strings using let for a mutable variable.
 * @returns {string} The combined string.
 */
export function taskNext() {
  let combination = 'But sometimes let';
  combination += getLast();

  return combination;
}
