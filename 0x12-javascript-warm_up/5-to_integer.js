#!/usr/bin/node
// 5. An Integer

const args = process.argv[2];
const arg1 = Math.floor(Number(args));
if (isNaN(arg1)) {
  console.log('My number: Not a number');
} else {
  console.log('My number:' + ' ' + arg1);
}
