#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};

for (const value of valsUniq) {
  const list = totalist.reduce((acc, [key, val]) => {
    if (val === value) {
      acc.unshift(key);
    }
    return acc;
  }, []);
  newDict[value] = list;
}

console.log(newDict);
