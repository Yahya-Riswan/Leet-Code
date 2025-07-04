/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    const set = {};

    for (const item of this) {
        const key = fn(item);
        if (!set[key]) {
            set[key] = [];
        }
        set[key].push(item);
    }

    return set;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */