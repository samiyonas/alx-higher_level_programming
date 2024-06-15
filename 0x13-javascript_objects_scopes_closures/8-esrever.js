#!/usr/bin/node
exports.esrever = function (list) {
  let i;
  let j;
  let temp;
  for (i = 0, j = list.length - 1; i < list.length / 2; i++, j--) {
    temp = list[i];
    list[i] = list[j];
    list[j] = temp;
  }
  return list;
};
