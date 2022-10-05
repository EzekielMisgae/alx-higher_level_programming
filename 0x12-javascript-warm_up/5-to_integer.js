#!/usr/bin/node

const arg = parseInt(process.argv[2]);
if (arg) {
	console.log('My number: ' + arg);
}
else{
	conole.log('Not a number');
}
