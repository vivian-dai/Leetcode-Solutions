# Day 4 - Apply Transform Over Each Element in Array
## Description
Given an integer array `arr` and a mapping function `fn`, return a new array with a transformation applied to each element.

The returned array should be created such that `returnedArray[i] = fn(arr[i], i)`.

Please solve it without the built-in `Array.map` method.

## Thought Process
1. "Hmmm recursion" because CS 135 broke me
2. "....wait iteration is a thing"

Turns out JS ignores extra arguments that functions don't use if it gets passed in