class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = [False] * 26
        upper = [False] * 26
        for c in word:
            if c.islower():
                if lower[ord(c) - ord('a')] is not None:
                    lower[ord(c) - ord('a')] = True
                if upper[ord(c) - ord('a')]:
                    lower[ord(c) - ord('a')] = False
                    print("bruh")
            elif c.isupper():
                if lower[ord(c) - ord('A')]:
                    upper[ord(c) - ord('A')] = True
                else:
                    lower[ord(c) - ord('A')] = None
        
        count = 0
        for i in range(26):
            if lower[i] and upper[i]:
                count += 1
        return count


print(Solution().numberOfSpecialChars("AbcbDBdD")) # 2
