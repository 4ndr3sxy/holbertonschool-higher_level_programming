#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    console.log(this.printRecursion(this.height, this.width, ''));
  }

  rotate () {
    const temporal = this.height;
    this.height = this.width;
    this.width = temporal;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }

  printRecursion (valueX, valueY, result) {
    const resultAdd = 'X';
    if (valueX > 0) {
      result += resultAdd.repeat(valueY);
      result += '\n';
      return (this.printRecursion(valueX - 1, valueY, result));
    } else {
      result = result.slice(0, -1);
      return result;
    }
  }
}

module.exports = Rectangle;
