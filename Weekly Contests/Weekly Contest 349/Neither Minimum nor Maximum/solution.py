class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:  # noqa: F821
        nums.sort()
        mini = nums[0]
        maxi = nums[-1]
        count = 0
        for num in nums:
            if (num != mini) and (num != maxi):
                return num
        return -1