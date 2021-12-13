#!/usr/bin/node
function add(a, b)
{
    let result = parseInt(a) + parseInt(b)
    console.log(result)
}

const arg = process.argv.slice(2)
add(arg[0], arg[1])
