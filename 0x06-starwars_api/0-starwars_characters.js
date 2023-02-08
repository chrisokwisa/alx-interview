#!/usr/bin/node

const https = require('https');

// The first positional argument passed is the Movie ID
const movieId = process.argv[2];

// API URL to retrieve details of the specified movie
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

https.get(apiUrl, (res) => {
  let data = '';
  res.on('data', (chunk) => {
    data += chunk;
  });
  res.on('end', () => {
    const movie = JSON.parse(data);
    const characters = movie.characters;
    characters.forEach((character) => {
      https.get(character, (res) => {
        let data = '';
        res.on('data', (chunk) => {
          data += chunk;
        });
        res.on('end', () => {
          const characterDetails = JSON.parse(data);
          console.log(characterDetails.name);
        });
      });
    });
  });
});
