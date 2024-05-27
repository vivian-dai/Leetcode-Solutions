class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        nums.sort()
        twice = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1] and nums[i] not in twice:
                twice.append(nums[i])
        xor = 0
        for t in twice:
            xor = xor ^ t
        return xor
