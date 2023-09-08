class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []
        for i in range(m):
            line = []
            for j in range(n):
                line.append(0)
            grid.append(line)
        for i in range(m):
            grid[i][0] = 1
        for i in range(n):
            grid[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[m - 1][n - 1]
        