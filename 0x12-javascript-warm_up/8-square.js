#!/usr/bin/node
function square(count, value)
{
    if (count === 0)
    {
        console.log(value);
    }
    else
    {
        count--;
        value += 'X';
        square(count, value);
    }
}

const arg = process.argv.slice(2);
if (isNaN(arg[0]))
    console.log('Missing size');
else
    for (let i = 0; i < arg[0]; i++) {
        square(arg[0], "");
    }

