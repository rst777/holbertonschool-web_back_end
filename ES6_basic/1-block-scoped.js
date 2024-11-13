/**
 * Creates two variables and returns them in an array.
 * Demonstrates block scoping with 'let'.
 */
export default function taskBlock(trueOrFalse) {
  let task = false;
  let task2 = true;

  // Always returns the original values
  return [task, task2];
}
