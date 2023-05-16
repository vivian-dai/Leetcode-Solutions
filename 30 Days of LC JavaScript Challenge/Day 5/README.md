# Day 5 - Filter Elements from Array
## Description
Given an integer array `arr` and a filtering function `fn`, return a new array with a fewer or equal number of elements.

The returned array should only contain elements where `fn(arr[i], i)` evaluated to a truthy value.

Please solve it without the built-in `Array.filter` method.
## Solution
Basically same approach as day 4 except using a new array and pushing elements in instead of overwriting the original array.