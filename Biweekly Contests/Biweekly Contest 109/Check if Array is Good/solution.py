class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) - 1 != nums[-1]:
            return False
        for i in range(len(nums) - 1):
            if nums[i] != i + 1:
                return False
        if nums[-1] != nums[-2]:
            return False
        else:
            return True
