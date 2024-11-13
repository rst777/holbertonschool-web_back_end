/**
 * Creates a report object containing all employees and a method to get the number of departments.
 *
 * @param {Object} employeesList - An object mapping department names to arrays of employee names.
 * @returns {Object} An object containing all employees and a method to count the departments.
 */
export default function createReportObject(employeesList) {
  return {
    allEmployees: {
      ...employeesList
    },
    /**
     * Returns the number of departments in the allEmployees object.
     * @returns {number} The number of departments.
     */
    getNumberOfDepartments() {
      return Object.keys(this.allEmployees).length;
    }
  };
}
