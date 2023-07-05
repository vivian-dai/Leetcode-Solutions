class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if gcd(nums[i], nums[j]) == 1:
                    count += 1
        return count
        