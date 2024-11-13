/**
 * Creates a budget object using object property shorthand syntax.
 *
 * @param {number} income - The income value.
 * @param {number} gdp - The GDP value.
 * @param {number} capita - The per capita value.
 * @returns {Object} An object containing the budget information.
 */
export default function getBudgetObject(income, gdp, capita) {
  const budget = {
    income,
    gdp,
    capita
  };

  return budget;
}
