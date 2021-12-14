#!/usr/bin/node
const fs = require('fs');
const arg = process.argv.slice(2);
let result = '';
fs.readFile(arg[0], function (err1, file1) {
  if (err1) throw err1;
  result += file1;
});
fs.readFile(arg[1], function (err2, file2) {
  if (err2) throw err2;
  result += file2;
  fs.writeFile(arg[2], result, function (err3) {
    if (err3) throw err3;
  });
});
