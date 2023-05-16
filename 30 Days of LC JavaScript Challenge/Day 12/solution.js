/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
	return async function(...args) {
        console.log(t)
        const resolved = new Promise((resolve) => resolve(fn(...args)));
        const rejected = new Promise((resolve, reject) => {
            setTimeout(() => {reject("Time Limit Exceeded")}, t)
            });
        return Promise.race([resolved, rejected]).then(result => {return result});
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */