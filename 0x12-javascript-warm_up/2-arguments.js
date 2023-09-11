#!/usr/bin/node

const process = require('process');
const args = process.argv.slice(2);
if (args.length === 1) {
  console.log('Argument found');
} else if (args.length > 1) {
  console.log('Arguments found');
} else if ((args.length === 0)) {
  console.log('No argument');
}
