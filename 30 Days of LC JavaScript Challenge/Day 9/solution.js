/**
 * @param {Function} fn
 */
function memoize(fn) {
    let mem = new Map();
    return function(...args) {
        let key = JSON.stringify(args);
        let val = mem.get(key);
        if(val === undefined) {
            mem.set(key, fn(...args));
        }
        return mem.get(key);
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