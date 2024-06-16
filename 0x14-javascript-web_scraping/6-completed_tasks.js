#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const cont = JSON.parse(body);
  const data = {};
  for (let i = 0; i < cont.length; i++) {
    if (cont[i].completed === true) {
      if (data[cont[i].userId] === undefined) {
        data[cont[i].userId] = 0;
      }
      data[cont[i].userId]++;
    }
  }
  console.log(data);
});
