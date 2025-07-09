/**
 * @param {Object} context
 * @param {Array} args
 * @return {null|boolean|number|string|Array|Object}
 */
Function.prototype.callPolyfill = function(context, ...args) {
    context = context || globalThis;


    const fnKey = Symbol();
    context[fnKey] = this;

 
    const result = context[fnKey](...args);

    delete context[fnKey];

    return result;
}

/**
 * function increment() { this.count++; return this.count; }
 * increment.callPolyfill({count: 1}); // 2
 */