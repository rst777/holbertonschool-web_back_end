/**
 * Initializes an array of classroom objects with specified sizes.
 *
 * @returns {Array} An array containing three ClassRoom objects with sizes 19, 20, and 34.
 */
import ClassRoom from './0-classroom.js';

export default function initializeRooms() {
  return [
    new ClassRoom(19),
    new ClassRoom(20),
    new ClassRoom(34)
  ];
}
