class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        one_distance = 0
        n_distance = 0
        found_one = False
        for i in range(n):
            if nums[i] == 1:
                one_distance = i
                found_one = True
            elif nums[i] == n:
                n_distance = n - i - 1
                if not found_one:
                    n_distance -= 1
        return one_distance + n_distance
