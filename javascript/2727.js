/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    if( 2 < JSON.stringify(obj).length){
        return false
    }else{
        return true
    }
};