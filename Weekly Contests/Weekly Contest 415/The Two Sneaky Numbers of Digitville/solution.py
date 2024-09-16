class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        sneks = []
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                sneks.append(nums[i])
        return sneks
