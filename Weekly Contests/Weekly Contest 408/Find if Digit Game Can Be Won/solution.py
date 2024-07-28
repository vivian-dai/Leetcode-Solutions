class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_sum = 0
        double_sum = 0
        for num in nums:
            if num >= 0 and num <= 9:
                single_sum += num
            else:
                double_sum += num
        return single_sum != double_sum
