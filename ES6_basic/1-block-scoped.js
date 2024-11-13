/**
 * Creates two variables and returns them in an array.
 * Demonstrates block scoping with 'let'.
 */
export default function taskBlock(trueOrFalse) {
  let task = false;
  let task2 = true;

  if (trueOrFalse) {
    // These variables are scoped to this block and don't affect outer variables
    let Task = true;
    let Task2 = false;
  }

  // Always returns the original values
  return [task, task2];
}
