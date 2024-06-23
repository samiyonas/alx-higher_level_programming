#!/usr/bin/node
$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: function (response) {
    response.results.forEach(function (resp) {
      $('#list_movies').append(`<li>${resp.title}`);
    });
  }
});
