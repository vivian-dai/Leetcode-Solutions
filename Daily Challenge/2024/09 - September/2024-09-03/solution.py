class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s1 = ""
        for c in s:
            s1 += str(ord(c) - ord('a') + 1)
        for i in range(k):
            s2 = 0
            for c in s1:
                s2 += int(c)
            s1 = str(s2)
        return int(s1)
