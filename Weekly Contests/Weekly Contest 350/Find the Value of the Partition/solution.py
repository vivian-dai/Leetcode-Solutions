class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        min_part = nums[1] - nums[0]
        for i in range(2, len(nums)):
            min_part = min(min_part, nums[i] - nums[i - 1])
        return min_part
        