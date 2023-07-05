class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        counts = []
        cur_count = 0
        for num in nums:
            if num == 0:
                counts.append(cur_count)
                cur_count = 0
            else:
                cur_count += 1
        counts.append(cur_count)
        if len(counts) == 0:
            return 0
        elif len(counts) == 1:
            return counts[0] - 1
        else:
            max_sum = counts[0] + counts[1]
            for i in range(2, len(counts)):
                sum = counts[i] + counts[i - 1]
                if sum > max_sum: max_sum = sum
            return max_sum
