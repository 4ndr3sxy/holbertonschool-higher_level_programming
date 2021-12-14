#!/usr/bin/node
const dict = require('./101-data').dict;
const dictArray = [];
const valuesDict = Object.values(dict);
const keyDict = Object.keys(dict);
dictArray[0] = valuesDict;
dictArray[1] = keyDict;
let newArray = [];

newArray = recursionDiff(valuesDict, 0, newArray);
let newDict = {};
let dictTemporal = [];
for (let i = 0; i < newArray.length; i++) {
  newDict = recursionNewDict(newDict, newArray[i], dict, dictArray[1], dictTemporal, 0);
  dictTemporal = [];
}
console.log(newDict);

function recursionDiff (values, iterator, arrayDiff) {
  if (values[iterator] !== undefined) {
    if (arrayDiff.indexOf(values[iterator]) < 0) {
      arrayDiff.push(values[iterator]);
    }
    return recursionDiff(values, iterator + 1, arrayDiff);
  }
  return arrayDiff;
}

function recursionNewDict (newDict, valueFind, dict, keys, arrayKey, iterator) {
  if (keys[iterator] !== undefined) {
    if (dict[keys[iterator]] === valueFind) {
      arrayKey.push(keys[iterator]);
    }
    return recursionNewDict(newDict, valueFind, dict, keys, arrayKey, iterator + 1);
  }
  newDict[valueFind] = arrayKey;
  return newDict;
}
