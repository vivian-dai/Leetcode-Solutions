class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] < nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
