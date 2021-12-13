#!/usr/bin/node
const arg = process.argv.slice(2);
const arg0 = arg[0] || 'undefined';
const arg1 = arg[1] || 'undefined';
console.log(arg0 + ' is ' + arg1);
