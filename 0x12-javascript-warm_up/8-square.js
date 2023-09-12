#!/usr/bin/node
const args = process.argv.slice(2);
const num = Number(args[0]);
const char = 'X'.repeat(num);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(args[0]); i++) {
    console.log(char);
  }
}
