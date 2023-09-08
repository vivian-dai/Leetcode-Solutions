class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        triangle.append([1])
        if numRows >= 2:
            triangle.append([1, 1])
        for i in range(2, numRows):
            row = []
            row.append(1)
            for j in range(1, i):
                row.append(triangle[i - 1][j] + triangle[i - 1][j - 1])
            row.append(1)
            triangle.append(row)
        return triangle
