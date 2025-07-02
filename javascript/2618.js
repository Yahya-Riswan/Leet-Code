/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (obj == null || typeof classFunction !== "function") {
        return false;
    }

    let prototype = classFunction.prototype;
    if (prototype == null) {

        return false;
    }

 
    let proto = Object.getPrototypeOf(obj);
    while (proto !== null) {
        if (proto === prototype) {
            return true;
        }
        proto = Object.getPrototypeOf(proto);
    }

    return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */