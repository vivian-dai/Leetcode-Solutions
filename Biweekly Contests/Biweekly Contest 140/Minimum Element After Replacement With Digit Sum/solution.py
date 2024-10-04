class Solution:
    def minElement(self, nums: List[int]) -> int:
        sums = []
        for num in nums:
            num = str(num)
            total = 0
            for c in num:
                total += ord(c) - ord('0')
            sums.append(total)
        minimum = sums[0]
        for s in sums:
            minimum = min(minimum, s)
        return minimum
