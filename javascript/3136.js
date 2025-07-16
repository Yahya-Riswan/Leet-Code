/**
 * @param {string} word
 * @return {boolean}
 */
var isValid = function(word) {
    if (word.length < 3) return false;

    // Check for invalid characters (only letters and digits allowed)
    if (!/^[a-zA-Z0-9]+$/.test(word)) return false;

    const vowels = /[aeiouAEIOU]/;
    const consonants = /[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]/;

    if (!vowels.test(word)) return false;
    if (!consonants.test(word)) return false;

    return true;

};