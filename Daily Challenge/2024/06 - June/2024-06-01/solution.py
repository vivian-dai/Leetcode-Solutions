class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s) - 1):
            left = ord(s[i])
            right = ord(s[i + 1])
            score += abs(right - left)
        return score
