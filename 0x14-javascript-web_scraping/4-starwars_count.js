#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const cont = JSON.parse(body);
  let counter = 0;
  for (let i = 0; i < cont.results.length; i++) {
    if (cont.results[i].characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      counter++;
    }
  }
  console.log(counter);
});
