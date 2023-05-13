# Day 8 - Allow One Function Call

## Description
Given a function `fn`, return a new function that is identical to the original function except that it ensures `fn` is called at most once.

* The first time the returned function is called, it should return the same result as `fn`.
* Every subsequent time it is called, it should return `undefined`.

## Thought Process
The function needs to return `undefined` after it's called once. What we can do is rewrite `fn` so that it returns `undefined`. This way, any calls to `fn` after are just calls to a function that returns `undefined`. 