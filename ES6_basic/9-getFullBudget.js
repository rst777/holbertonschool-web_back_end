import getBudgetObject from './7-getBudgetObject.js';

/**
 * Creates a full budget object with additional methods.
 *
 * @param {number} income - The income value.
 * @param {number} gdp - The GDP value.
 * @param {number} capita - The per capita value.
 * @returns {Object} An object containing budget information and methods to format income.
 */
export default function getFullBudgetObject(income, gdp, capita) {
  const budget = getBudgetObject(income, gdp, capita);
  const fullBudget = {
    ...budget,
    /**
     * Formats the income in dollars.
     * @param {number} income - The income to format.
     * @returns {string} The income formatted in dollars.
     */
    getIncomeInDollars(income) {
      return `$${income}`;
    },
    /**
     * Formats the income in euros.
     * @param {number} income - The income to format.
     * @returns {string} The income formatted in euros.
     */
    getIncomeInEuros(income) {
      return `${income} euros`;
    },
  };

  return fullBudget;
}
