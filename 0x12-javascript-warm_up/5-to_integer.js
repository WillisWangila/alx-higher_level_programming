#!/usr/bin/node

const process = require('process');
const args = process.argv.slice(2);
if (parseInt(args[0])) {
  console.log('My number: ', args[0]);
} else {
  console.log('Not a number');
}
