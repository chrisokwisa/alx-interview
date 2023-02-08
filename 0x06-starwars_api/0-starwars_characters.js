#!/usr/bin/node

const process = require('process');
const request = require('request');

// Get the movie ID from the command line argument
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

// Make a request to the API to get the details of the movie
request(url, 'utf-8', async (err, resp, body) => {
  if (!err) {
    const movie = JSON.parse(body);
    const chars = movie.characters;

    // Create a new promise that returns the details of a character
    const newPromise = (url) => {
      return new Promise(function (resolve, reject) {
        request(url, 'utf-8', (err, resp, body) => {
          if (err) reject(err);
          else resolve(body);
        });
      });
    };

    // Loop through the list of characters and print their names
    for (const each in chars) {
      const actor = await newPromise(chars[each]);
      const charList = JSON.parse(actor);
      console.log(charList.name);
    }
  }
});
