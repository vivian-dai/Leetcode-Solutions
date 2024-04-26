from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = -2147483649
        second = -2147483649
        third = -2147483649
        for i in range(len(nums)):
            if nums[i] > first:
                third = second
                second = first
                first = nums[i]
            elif nums[i] > second and nums[i] != first:
                third = second
                second = nums[i]
            elif nums[i] > third and nums[i] != second and nums[i] != first:
                third = nums[i]
        if third != -2147483649:
            return third
        else:
            return first
        
print(Solution().thirdMax([2, 2, 3, 1]))
