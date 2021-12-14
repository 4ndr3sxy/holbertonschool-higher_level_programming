#!/usr/bin/node
var concat = require('concat-files');

const arg = process.argv.slice(2);

concat([
  arg[0],
  arg[1]
], arg[2], function (err) {
  if (err) throw err
  console.log('done');
});
