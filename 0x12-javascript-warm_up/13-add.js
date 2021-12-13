#!/usr/bin/node

function add (a, b) {
  const result = parseInt(a) + parseInt(b);
  return result;
}

module.exports.add = add;
