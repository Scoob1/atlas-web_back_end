export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Method to clone car
  cloneCar() {
    const NewCar = this.constructor[Symbol.species] || this.constructor;
    return new NewCar();
  }

  // Define Symbol.species for the cloning
  static get [Symbol.species]() {
    return this;
  }
}
