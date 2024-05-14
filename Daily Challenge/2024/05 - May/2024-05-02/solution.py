class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        lar = len(nums) - 1
        neg = 0
        while lar >= neg:
            if nums[lar] == abs(nums[neg]) and nums[neg] < 0:
                return nums[lar]
            elif nums[lar] > abs(nums[neg]):
                lar -= 1
            else:
                neg += 1
        return -1
