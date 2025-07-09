/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if (Array.isArray(obj)) {
        return obj
            .map(compactObject)             // Recursively process children
            .filter(Boolean);               // Remove falsy values
    } else if (obj !== null && typeof obj === 'object') {
        const result = {};
        for (const [key, value] of Object.entries(obj)) {
            const compacted = compactObject(value);
            if (Boolean(compacted)) {
                result[key] = compacted;
            }
        }
        return result;
    } else {
        return obj;
    }
};