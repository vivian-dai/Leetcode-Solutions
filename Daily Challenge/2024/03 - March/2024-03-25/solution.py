from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * (n + 1) # counts number of items in list
        for num in nums:
            count[num] += 1
        ret_arr = []
        for i in range(n + 1):
            if count[i] > 1:
                ret_arr.append(i)
        return ret_arr
