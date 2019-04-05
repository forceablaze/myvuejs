'use strict'
let delay = (ms) => {
  return (result) => {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve(result);
      }, ms);
    });
  };
}

let retry = (func) => {
  return (ms) => {
    func()
    .then((r) => {
      console.log(r);
      resolve(r);
    })
    .catch((err) => {
      delay(ms)('retry').then((result) => {
        retry(func)(ms);
      });
    });
  }
}

let reverse = (str) => {
  return [...str].reverse().join('')
}

let isVisableASCII = (str) => {
  return /^[\x20-\x7E]*$/.test(str);
}

export { delay, reverse };
