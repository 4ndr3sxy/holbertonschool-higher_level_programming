#!/usr/bin/node
const arg = process.argv.slice(2)
const number = parseInt(arg[0])
if (isNaN(number))
    console.log('Not a number')
else
    console.log('My number: ' + number)
