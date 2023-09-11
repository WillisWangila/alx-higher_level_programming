#!/usr/bin/node

const process = require('process');
const args = process.argv.slice(2);
const is = ' is ';
const noVal = 'undefined';
if (args[0] && args[1]) {
  console.log(args[0].concat(is, args[1]));
} else if (args.length === 0) {
  console.log(noVal.concat(is, noVal));
} else {
  console.log(args[0].concat(is, noVal));
}
