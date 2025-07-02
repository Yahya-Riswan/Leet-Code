/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn,memo={}) {
    return function(...args) {
        let id=JSON.stringify(args)
        if(id in memo){
            return memo[id]
        }
        let x=fn(...args)
        memo[id]=x
        return x;

    }
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