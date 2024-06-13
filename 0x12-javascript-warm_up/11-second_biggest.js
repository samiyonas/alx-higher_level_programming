#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let arr = process.argv.slice(2);
  arr = arr.sort((a, b) => a - b);
  console.log(arr[arr.length - 2]);
}