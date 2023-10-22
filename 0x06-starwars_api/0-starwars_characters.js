#!/usr/bin/node
const request = require('request');

function getData(url) {
    return new Promise((resolve, reject) => {
        request(url, (err, res, body) => {
            if (err) {
                reject(err);
            } else if (res.statusCode !== 200) {
                reject( Error('Error'));
            } else{
            resolve(JSON.parse(body));
            }
        });
    });
}
function getchar(char) {
    const promise = char.map(charUrl => getData(charUrl));
    return Promise.all(promise);
}
request('https://swapi-api.hbtn.io/api/films' + process.argv[2], (err, res, body) => {
    if (err) {
        console.log(err);
    }
    const char = JSON.parse(body).characters;
    getchar(char)
    .then(charData => {
        console.log(charData);
    }).catch(error => {
        console.log(error);
    });
});

