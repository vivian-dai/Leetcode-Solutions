class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        mappings = {}
        for s in arr:
            if s in mappings:
                mappings[s] += 1
            else:
                mappings[s] = 1
        for s in arr:
            if mappings[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ""
