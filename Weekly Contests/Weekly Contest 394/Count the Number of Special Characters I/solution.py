class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = [False] * 26
        upper = [False] * 26
        for c in word:
            if c.islower():
                lower[ord(c) - ord('a')] = True
            elif c.isupper():
                upper[ord(c) - ord('A')] = True
        
        count = 0
        for i in range(26):
            if lower[i] and upper[i]:
                count += 1
        return count
