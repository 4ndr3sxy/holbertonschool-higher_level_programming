#!/usr/bin/node

const args = process.argv;
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + args[2], function (err, requestFilm) {
  if (err) {
    console.error(err);
    return;
  }
  const json = JSON.parse(requestFilm.body);
  json.characters.forEach(element => {
    const fetch = new Promise((resolve, reject) => {
      request(element, (err, requestChar) => {
        if (err) {
          console.error(err);
          return;
        }
        const jsonCharacter = JSON.parse(requestChar.body);
        resolve(jsonCharacter.name);
      });
    });
    fetch.then((val) => console.log(val));
  });
});
