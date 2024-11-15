/**
 * Creates two variables and returns them in an array.
 * Demonstrates block scoping with 'let'.
 */
export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    console.log(task, task2);
    return [task, task2];
  }

  // Always returns the original values
  return [task, task2];
}
