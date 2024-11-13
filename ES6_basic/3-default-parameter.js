/**
 * Calculates the sum of the initial number and two expansion values.
 *
 * @param {number} initialNumber - The initial number to start with.
 * @param {number} [expansion1989=89] - The 1989 expansion value, defaults to 89.
 * @param {number} [expansion2019=19] - The 2019 expansion value, defaults to 19.
 * @returns {number} The sum of initialNumber, expansion1989, and expansion2019.
 */
export default function getSumOfHoods(initialNumber, expansion1989 = 89, expansion2019 = 19) {
  return initialNumber + expansion1989 + expansion2019;
}
