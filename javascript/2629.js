/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {

    return function(x) {
        let rs = x;
        for(let i = functions.length - 1; i>=0; i--){
            rs = functions[i](rs);
        }
        return rs
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */