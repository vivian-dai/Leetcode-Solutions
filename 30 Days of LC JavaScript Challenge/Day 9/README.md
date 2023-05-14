# Day 9 - Memoize

## Description
Given a function `fn`, return a memoized version of that function.

A memoized function is a function that will never be called twice with the same inputs. Instead it will return a cached value.

You can assume there are 3 possible input functions: `sum`, `fib`, and `factorial`.

* `sum` accepts two integers `a` and `b` and returns `a + b`.
* `fib` accepts a single integer `n` and returns `1` if `n <= 1` or `fib(n - 1) + fib(n - 2)` otherwise.
* `factorial` accepts a single integer `n` and returns `1` if `n <= 1` or `factorial(n - 1) * n` otherwise.

## Notes
I had
```js
return function(...args) {
    let mem = new Map();
    let key = JSON.stringify(args);
    let val = mem.get(key);
    if(val === undefined) {
        mem.set(key, fn(...args));
    }
    return mem.get(key);
}
```
for a while and kept trying to debug that before realizing the map was out of scope