#!/usr/bin/node
const args = process.argv.slice(2);
num = Number(args[0]);
function factorial (n) {
  if (n === 0 || isNaN(n)) return 1;
  return n * factorial(n - 1);
}
console.log(factorial(num));
