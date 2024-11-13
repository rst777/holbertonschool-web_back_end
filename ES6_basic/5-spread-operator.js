/**
 * Concatenates two arrays and each character of a string into a single array.
 *
 * @param {Array} array1 - The first array to concatenate.
 * @param {Array} array2 - The second array to concatenate.
 * @param {string} string - The string to split into individual characters and concatenate.
 * @returns {Array} A new array containing all elements from array1, array2, and each character of the string.
 */
export default function concatArrays(array1, array2, string) {
  return [...array1, ...array2, ...string];
}
