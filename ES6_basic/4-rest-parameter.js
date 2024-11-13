/**
 * Returns the number of arguments passed to the function.
 *
 * @param {...*} args - Any number of arguments of any type.
 * @returns {number} The count of arguments passed to the function.
 */
export default function returnHowManyArguments(...args) {
  return args.length;
}
