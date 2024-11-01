class Solution:
    def maxScore(self, nums: List[int]) -> int:
        def lcm(numbers):
            return reduce(lambda x, y: x * y // math.gcd(x, y), numbers, 1)
        def gcd(numbers):
            if not numbers:
                return 1
            return reduce(lambda x, y: math.gcd(x, y), numbers)
        max_c = lcm(nums) * gcd(nums)
        for i in range(len(nums)):
            new_nums = nums[:i] + nums[i+1:]
            c = lcm(new_nums) * gcd(new_nums)
            max_c = max(max_c, c)
        return max_c