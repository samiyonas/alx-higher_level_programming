#!/usr/bin/node
const request = require('request');

url = 'https://swapi-api.alx-tools.com/api/people/18/';
request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const cont = JSON.parse(body);
  let counter = 0;
  cont.results.forEach((films) => {
    if (films.characters.includes(url)){
      counter++;
    }
  })
  console.log(counter);
});
