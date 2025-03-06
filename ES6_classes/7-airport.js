export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  // toString method
  toString() {
    return `[object ${this._code}]`;
  }
}
