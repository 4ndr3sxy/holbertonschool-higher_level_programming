#!/usr/bin/node
function factorialR (num) {
    if (num === 1 || isNaN(num)) {
        return 1;
    } else {
        return num * factorial_r(num - 1);
    }
}

const arg = process.argv.slice(2);
console.log(factorialR(parseInt(arg[0])));
