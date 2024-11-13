/**
 * Gets the current year.
 *
 * @returns {number} The current year.
 */
function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

/**
 * Creates a budget object for the current year using computed property names.
 *
 * @param {number} income - The income value.
 * @param {number} gdp - The GDP value.
 * @param {number} capita - The per capita value.
 * @returns {Object} An object containing the budget information for the current year.
 */
export default function getBudgetForCurrentYear(income, gdp, capita) {
  return {
    [`income-${getCurrentYear()}`]: income,
    [`gdp-${getCurrentYear()}`]: gdp,
    [`capita-${getCurrentYear()}`]: capita
  };
}
