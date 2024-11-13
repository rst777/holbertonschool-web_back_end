/**
 * Creates two variables and returns them in an array.
 * Demonstrates block scoping with 'let'.
 *
 * @param {boolean} trueOrFalse - Determines if the inner block is executed.
 * @returns {Array} An array containing two boolean values.
 */
export default function taskBlock(trueOrFalse) {
  let task = false;
  let task2 = true;

  if (trueOrFalse) {
    // These variables are scoped to this block and don't affect outer variables
    let innerTask = true;
    let innerTask2 = false;
    // Inner block variables can be used here if needed
  }

  // Always returns the original values
  return [task, task2];
}
