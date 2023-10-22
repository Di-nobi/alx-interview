#!/usr/bin/node
// const request = require('request');

// function getData(url) {
//     return new Promise((resolve, reject) => {
//         request(url, (err, res, body) => {
//             if (err) {
//                 reject(err);
//             } else if (res.statusCode !== 200) {
//                 reject( Error('Error'));
//             } else{
//             resolve(JSON.parse(body));
//             }
//         });
//     });
// }
// function getchar(char) {
//     const promise = char.map(charUrl => getData(charUrl));
//     return Promise.all(promise);
// }
// request('https://swapi-api.hbtn.io/api/films' + process.argv[2], (err, res, body) => {
//     if (err) {
//         console.log(err);
//     }
//     const char = JSON.parse(body).characters;
//     getchar(char)
//     .then(charData => {
//         console.log(charData);
//     }).catch(error => {
//         console.log(error);
//     });
// });

#!/usr/bin/node
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    // for (const character of characters) {
    //   request(character, function (error, response, body) {
    //     if (error) {
    //       console.log(error);
    //     } else {
    //       console.log(JSON.parse(body).name);
    //     }
    //   });
    // }
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  request(characters[index], function (err, response, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
