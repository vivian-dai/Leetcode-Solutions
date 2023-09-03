class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acc = ""
        for word in words:
            acc += word[0]
        return acc == s
        