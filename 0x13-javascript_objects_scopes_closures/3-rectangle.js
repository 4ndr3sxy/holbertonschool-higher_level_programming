#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const value = this.height;
    console.log(this.printRecursion(value, ''));
  }

  printRecursion (value, result) {
    const resultAdd = 'X';
    if (value > 0) {
      result += resultAdd.repeat(this.width);
      result += '\n';
      return (this.printRecursion(value - 1, result));
    } else {
      result = result.slice(0, -1);
      return result;
    }
  }
}

module.exports = Rectangle;
