#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return recursion(list, searchElement, 0, 0);
};

function recursion (list, element, iterator, ocurrences) {
  if (list[iterator] === undefined) {
    return ocurrences;
  } else {
    if (list[iterator] === element) {
      ocurrences++;
    }
    return recursion(list, element, iterator + 1, ocurrences);
  }
}
