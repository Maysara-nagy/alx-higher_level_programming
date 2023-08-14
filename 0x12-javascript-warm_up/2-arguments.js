#!/usr/bin/node
// Write a script that prints a message depending of the number of arguments passed:

const args1 = process.argv.length;
console.log(args1 === 2 ? 'No argument' : args1 === 3 ? 'Argument found' : 'Arguments found');
