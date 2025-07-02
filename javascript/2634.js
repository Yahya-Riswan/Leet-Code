/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let _array = []
  arr.forEach((item,i) => {
    if(fn(item, i)){
      _array.push(item);
    }
  })
  return _array;
};