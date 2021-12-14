#!/usr/bin/node
let index = 0;
const list = require('./100-data').list;
console.log(list);
const newList = list.map(function (value) {
  const result = value * index;
  index++;
  return result;
});
console.log(newList);
