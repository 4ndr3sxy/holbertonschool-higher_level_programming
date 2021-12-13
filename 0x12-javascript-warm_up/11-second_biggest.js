#!/usr/bin/node
function second_biggest(args)
{
    let biggest = 0;
    let second = 0;
    args.forEach(element => {
        if (parseInt(element) > biggest)
            biggest = element
    });
    args.forEach(element => {
        if (parseInt(element) > second && element !== biggest)
        {
            second = element
        }
    });
    return second
}

const arg = process.argv.slice(2)
const countArg = Object.keys(arg).length
switch (countArg)
{
    case 0:
    case 1:
        console.log(0)
        break
    default:
        console.log(second_biggest(arg))
        break
}
