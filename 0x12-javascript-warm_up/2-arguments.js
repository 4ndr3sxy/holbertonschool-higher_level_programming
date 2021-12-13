#!/usr/bin/node
const arg = process.argv.slice(2);
const countArg = Object.keys(arg).length;
switch (countArg) {
	case 0:
		console.log('No argument');
		break;
	case 1:
		console.log('Argument found');
		break;
	default:
		console.log('Arguments found');
		break;
}
