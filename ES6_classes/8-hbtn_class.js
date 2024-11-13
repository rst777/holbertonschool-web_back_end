/**
 * Class representing a Holberton class.
 */
export default class HolbertonClass {
  /**
   * Creates an instance of HolbertonClass.
   *
   * @param {number} size - The size of the class.
   * @param {string} location - The location of the class.
   */
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  /**
   * Returns the size when the instance is converted to a number.
   *
   * @returns {number} The size of the class.
   */
  valueOf() {
    return this._size;
  }

  /**
   * Returns the location when the instance is converted to a string.
   *
   * @returns {string} The location of the class.
   */
  toString() {
    return this._location;
  }
}
