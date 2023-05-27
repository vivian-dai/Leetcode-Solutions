class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:  # noqa: F821
        lowest = len(s)
        for word in dictionary:
            if word in s:
                lowest = min(lowest, self.minExtraChar("".join(s.split(word)), dictionary))
                
        return lowest
        