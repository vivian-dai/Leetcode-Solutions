class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:  # noqa: F821
        score = 0
        for i in range(len(nums[0])):
            max = nums[0][i]
            for j in range(len(nums)):
                if(nums[j][i] > max): 
                    max = nums[j][i]
                # print(nums[j])
            print(max)
            score += max
        return score