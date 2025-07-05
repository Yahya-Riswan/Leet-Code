var TimeLimitedCache = function() {
    this.cache = new Map();
};

TimeLimitedCache.prototype.set = function(key, value, duration) {
    const now = Date.now();
    const item = this.cache.get(key);
    const exists = item && item.expiry > now;

    this.cache.set(key, { value, expiry: now + duration });
    return !!exists;
};

TimeLimitedCache.prototype.get = function(key) {
    const now = Date.now();
    const item = this.cache.get(key);

    return item && item.expiry > now ? item.value : -1;
};

TimeLimitedCache.prototype.count = function() {
    const now = Date.now();
    let count = 0;

    for (const { expiry } of this.cache.values()) {
        if (expiry > now) count++;
    }

    return count;
};



/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */