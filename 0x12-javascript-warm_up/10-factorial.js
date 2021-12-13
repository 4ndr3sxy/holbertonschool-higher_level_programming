#!/usr/bin/node
const arg = process.argv.slice(2);
console.log(factorialR(parseInt(arg[0])));

function factorialR (num) {
    if (num === 1 || isNaN(num)) {
        return 1;
    } else {
        return (num * factorialR(num - 1));
    }
}

