/**
 * Creates an object with a list of neighborhoods and a method to add new ones.
 *
 * @returns {Object} An object with sanFranciscoNeighborhoods array and addNeighborhood method.
 */
export default function getNeighborhoodsList() {
  this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

  /**
   * Adds a new neighborhood to the list and returns the updated list.
   *
   * @param {string} newNeighborhood - The name of the neighborhood to add.
   * @returns {Array} The updated list of neighborhoods.
   */
  this.addNeighborhood = (newNeighborhood) => {
    this.sanFranciscoNeighborhoods.push(newNeighborhood);
    return this.sanFranciscoNeighborhoods;
  };
}
