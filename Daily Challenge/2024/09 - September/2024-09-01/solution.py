class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != n * m:
            return []
        arr = []
        for i in range(m):
            line = []
            for j in range(n):
                line.append(original[i * n + j])
            arr.append(line)
        return arr
