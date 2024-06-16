#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const cont = JSON.parse(body);
  for (let i = 0; i < cont.characters.length; i++) {
    request.get(cont.characters[i], (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const anoCont = JSON.parse(body);
      console.log(anoCont.name);
    });
  }
});
