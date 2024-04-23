#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.slice(2, process.argv.length - 1);
  let max = Math.max(...list);
  let Secondmax = list[0];
  for (let i = 0; i < list.length; i++) {
    if (list[i] > Secondmax && list[i] > max) {
      Secondmax = list[i];
    }
  }
  console.log(Secondmax);
}
