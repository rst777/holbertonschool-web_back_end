export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand; // Stocke la marque dans une variable privée _brand
    this._motor = motor; // Stocke le moteur dans une variable privée _motor
    this._color = color; // Stocke la couleur dans une variable privée _color
  }

  // Méthode cloneCar : Crée une nouvelle instance de la classe
  cloneCar() {
    const Constructor = this.constructor[Symbol.species] || this.constructor;
    return new Constructor();
  }
}
