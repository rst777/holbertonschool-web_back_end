export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  // Getter pour code
  get code() {
    return this._code;
  }

  // Setter pour code
  set code(value) {
    this._code = value;
  }

  // Getter pour name
  get name() {
    return this._name;
  }

  // Setter pour name
  set name(value) {
    this._name = value;
  }

  // Méthode pour afficher la devise au format requis
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
