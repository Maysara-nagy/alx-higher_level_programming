#!/usr/bin/node
// Write a script that computes and prints a factorial

function fac (x) {
  if (isNaN(x)) {
    return 1;
  } if (x === 0) {
    return 1;
  } else {
    return x * fac(x - 1);
  }
}

console.log(fac(Number(process.argv[2])));
