/**
 * Appends a string to each value in an array.
 *
 * @param {Array} array - The input array of strings.
 * @param {string} appendString - The string to append to each array value.
 * @returns {Array} A new array with the appendString added to each original value.
 */
export default function appendToEachArrayValue(array, appendString) {
  const newArray = [];
  for (let value of array) {
    newArray.push(appendString + value);
  }
  return newArray;
}
