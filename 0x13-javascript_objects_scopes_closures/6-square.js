#!/usr/bin/node
const SquareI = require('./5-square');
class Square extends SquareI {
  charPrint (c) {
    let result = '';
    if (c !== undefined) {
      for (let i = 0; i < this.width; i++) {
        result += c.repeat(this.width) + '\n';
      }
      console.log(result.slice(0, -1));
    } else {
      this.print();
    }
  }
}

module.exports = Square;
