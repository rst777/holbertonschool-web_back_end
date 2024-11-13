/**
 * Class representing an airport.
 */
export default class Airport {
  /**
   * Creates an instance of Airport.
   *
   * @param {string} name - The name of the airport.
   * @param {string} code - The airport code.
   */
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  /**
   * Returns a string representation of the airport.
   *
   * @returns {string} A string in the format '[object CODE]'.
   */
  toString() {
    return `[object ${this._code}]`;
  }
}
