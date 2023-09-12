#!/usr/bin/node

const process = require('process');
const args = process.argv.slice(2);
let num = ''
if (num = Math.trunc(args[0])) {
  console.log('My number: ', num);
} else {
  console.log('Not a number');
}
