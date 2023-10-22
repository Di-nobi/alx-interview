#!/usr/bin/node
const request = require('request');
const api = 'https://swapi-api.hbtn.io/api/films';
request(api + process.argv[2], (err, res, body) => {
    if (err) {
        console.log(err);
    }
    const char = JSON.parse(body).characters;
    getchar(char);
});

getchar (char, idx) {
    request(char[idx], (err, res, body) => {

        if (idx + 1 < char.length) {
            getchar(char, idx + 1);
        }
    });
}