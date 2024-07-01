class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        min_avg = 51
        nums.sort()
        while len(nums) != 0:
            a = (nums[0] + nums[-1])/2
            del(nums[0])
            del(nums[-1])
            if a < min_avg: min_avg = a
        return min_avg
