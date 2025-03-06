export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // Method casting to Num
  valueOf() {
    return this._size;
  }

  // Method casting to Str
  toString() {
    return this._location;
  }
}
