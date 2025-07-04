/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const set = new Map();

    return function(...args) {
        let now = set;

        for (const arg of args) {
            if (!now.has(arg)) {
                now.set(arg, new Map());
            }
            now = now.get(arg);
        }

        if (now.has('result')) {
            return now.get('result');
        }

        const result = fn(...args);
        now.set('result', result);
        return result;
    };
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */