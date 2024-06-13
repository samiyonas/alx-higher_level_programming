#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let arr = process.argv.slice(2);
  arr = arr.sort();
  console.log(arr[arr.length - 2]);
}
