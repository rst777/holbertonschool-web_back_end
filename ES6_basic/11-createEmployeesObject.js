/**
 * Creates an object with a department name as the key and an array of employees as the value.
 *
 * @param {string} departmentName - The name of the department.
 * @param {string[]} employees - An array of employee names.
 * @returns {Object} An object with the department name as the key and the employees array as the value.
 */
export default function createEmployeesObject(departmentName, employees) {
  return {
    [departmentName]: employees
  };
}
