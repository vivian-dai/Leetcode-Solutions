class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = heights.copy()
        exp.sort()
        count = 0
        for i in range(len(heights)):
            if heights[i] != exp[i]:
                count += 1
        return count
