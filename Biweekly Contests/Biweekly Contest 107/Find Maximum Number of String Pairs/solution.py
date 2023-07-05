class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            s = (words[i])[::-1]
            for j in range(i + 1, len(words)):
                if s == words[j]:
                    count += 1
        return count
        