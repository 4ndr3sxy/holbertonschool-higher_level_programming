#!/usr/bin/node
const arg = process.argv.slice(2);
if (isNaN(arg[0]))
    console.log('Missing number of occurrences');
else
    for (let i = 0; i < arg[0]; i++) {
        console.log('C is fun');
    }

