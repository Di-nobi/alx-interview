#!/usr/bin/node
const request = require('request');
const api = 'https://swapi-api.hbtn.io/api/films/';

request(api + process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const chars = JSON.parse(body).characters;

    getChars(chars, 0);
  }
});

function getChars (chars, idx) {
    request(chars[idx], (err, res, body) => {
      if (err) {
        console.log(err);
      } else {
        console.log(JSON.parse(body).name);
        }

        if (idx + 1 < chars.length) {
          getChars(chars, idx + 1);
        }
    });
}
