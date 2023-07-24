class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        end = []
        for word in words:
            seps = word.split(separator)
            for j in seps:
                if j != "":
                    end.append(j)
        return end
