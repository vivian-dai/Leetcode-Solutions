class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s = list(s)
        t = list(t)
        sum = 0
        for i in range(len(s)):
            sum += abs(t.index(s[i]) - i)
        return sum
