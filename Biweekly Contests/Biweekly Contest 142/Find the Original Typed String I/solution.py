class Solution:
    def possibleStringCount(self, word: str) -> int:
        last_c = word[0]
        count = 0
        for c in word:
            if c == last_c:
                count += 1
            else:
                last_c = c
        return count