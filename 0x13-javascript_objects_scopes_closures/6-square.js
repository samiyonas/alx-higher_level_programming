#!/usr/bin/node
const sqr = require('./5-square');
module.exports = class Square extends sqr {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let i;
    for (i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
