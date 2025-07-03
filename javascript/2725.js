/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    fn(...args);
     const id = setInterval(() => {
        fn(...args);
    }, t);
    return () => {
        clearInterval(id);
    };
};