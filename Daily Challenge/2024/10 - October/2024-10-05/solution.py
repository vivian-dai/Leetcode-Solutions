class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window method
        if len(s2) < len(s1): return False
        letters_perm = [0] * 26
        letters_cur = [0] * 26
        for c in s1:
            letters_perm[ord(c) - ord('a')] += 1
        for i in range(len(s1)):
            letters_cur[ord(s2[i]) - ord('a')] += 1
        thing = True
        for i in range(26):
            if letters_perm[i] != letters_cur[i]:
                thing = False
        if thing:
            return True
        for i in range(len(s2) - len(s1)):
            letters_cur[ord(s2[i]) - ord('a')] -= 1
            letters_cur[ord(s2[i + len(s1)]) - ord('a')] += 1
            thing = True
            for j in range(26):
                if letters_perm[j] != letters_cur[j]:
                    thing = False
            if thing:
                return True
        return False
