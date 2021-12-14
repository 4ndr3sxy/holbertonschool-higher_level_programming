#!/usr/bin/node
exports.esrever = function (list) {
  const newList = new Array(list.length);
  return recursion(list, newList, 0, list.length - 1);
};

function recursion (list, newList, iterator, reverse) {
  if (list[iterator] !== undefined) {
    newList[reverse] = list[iterator];
    return recursion(list, newList, iterator + 1, reverse - 1);
  }
  return newList;
}
