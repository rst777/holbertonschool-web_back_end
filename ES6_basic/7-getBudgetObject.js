export default function getBudgetObject(income = 0, gdp = 0, capita = 0) {
  const budget = {
    income,
    gdp,
    capita,
  };

  return budget;
}
