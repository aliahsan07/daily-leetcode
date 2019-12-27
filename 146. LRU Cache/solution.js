/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
  this.cache = {};
  // this.leastRecentlyUsedKey = null;
  this.cap = capacity;
  this.counter = 1;
};

/**
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
  if (this.cache.hasOwnProperty(key)) {
    if (this.cache[key].tally != this.counter - 1) {
      this.cache[key].tally = this.counter;
      this.counter++;
    }
    return this.cache[key].value;
  }

  return -1;
};

/**
 * @param {number} key
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
  if (
    this.cache.hasOwnProperty(key) ||
    Object.keys(this.cache).length < this.cap
  ) {
    const tally = this.counter;
    this.cache[key] = { value, tally };
    this.counter++;
    return;
  }

  let found = this.getLRUKey();
  delete this.cache[found];
  this.put(key, value);
};

LRUCache.prototype.getLRUKey = function() {
  let min = Number.POSITIVE_INFINITY;
  let k = null;
  for (var key in this.cache) {
    if (this.cache[key].tally < min) {
      min = this.cache[key].tally;
      k = key;
    }
  }
  return k;
};
