class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid

    def adjacentSum(self, value: int) -> int:
        adj_sum = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == value:
                    # found value
                    if i > 0:
                        adj_sum += self.grid[i - 1][j]
                    if j > 0:
                        adj_sum += self.grid[i][j - 1]
                    if i < len(self.grid) - 1:
                        adj_sum += self.grid[i + 1][j]
                    if j < len(self.grid[0]) - 1:
                        adj_sum += self.grid[i][j + 1]
        return adj_sum

    def diagonalSum(self, value: int) -> int:
        diag_sum = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == value:
                    # found value
                    if i > 0 and j > 0:
                        diag_sum += self.grid[i - 1][j - 1]
                    if i < len(self.grid) - 1 and j < len(self.grid[0]) - 1:
                        diag_sum += self.grid[i + 1][j + 1]
                    if i > 0 and j < len(self.grid[0]) - 1:
                        diag_sum += self.grid[i - 1][j + 1]
                    if i < len(self.grid) - 1 and j > 0:
                        diag_sum += self.grid[i + 1][j - 1]
        return diag_sum


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
