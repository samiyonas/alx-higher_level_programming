#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.slice(2, process.argv.length);
  const arr = list.map(item => parseInt(item));
  const max = Math.max(...arr);
  let Secondmax = arr[0];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > Secondmax && arr[i] < max) {
      Secondmax = arr[i];
    }
  }
  console.log(Secondmax);
}
