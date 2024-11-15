import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  // Getter pour amount
  get amount() {
    return this._amount;
  }

  // Setter pour amount
  set amount(value) {
    this._amount = value;
  }

  // Getter pour currency
  get currency() {
    return this._currency;
  }

  // Setter pour currency
  set currency(value) {
    if (!(value instanceof Currency)) {
      throw new TypeError('currency must be an instance of Currency');
    }
    this._currency = value;
  }

  // Méthode pour afficher le prix au format requis
  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  // Méthode statique pour convertir le prix
  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
