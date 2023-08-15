#!/usr/bin/node
// Write a script that prints a square

const X = Math.floor(Number(process.argv[2]));
if (isNaN(X)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < X; i++) {
    for (let j = 0; j < i; j++) {
      console.log('X');
    }
    console.log('\n');
  }
}
