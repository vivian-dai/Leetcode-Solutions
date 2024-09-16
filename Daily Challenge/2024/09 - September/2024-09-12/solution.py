class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter = 0
        for word in words:
            good = True
            for letter in word:
                if not letter in allowed:
                    good = False
                    break
            if good:
                counter += 1
        return counter
