#!/usr/bin/node
// Write a script that prints a message depending of the number of arguments passed:

const args1 = process.argv.length;
if (args1 === 2) {
    console.log('No argument');
} else if (args1 === 3) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
