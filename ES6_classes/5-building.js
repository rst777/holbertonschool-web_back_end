/**
 * Class representing a building.
 */
export default class Building {
  /**
   * Creates an instance of Building.
   *
   * @param {number} sqft - The square footage of the building.
   */
  constructor(sqft) {
    this._sqft = sqft;
  }

  /**
   * Gets the square footage of the building.
   *
   * @returns {number} The square footage.
   */
  get sqft() {
    return this._sqft;
  }

  /**
   * Abstract method to display evacuation warning message.
   * Must be overridden by subclasses.
   *
   * @throws {Error} Throws an error if not implemented in subclass.
   */
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
