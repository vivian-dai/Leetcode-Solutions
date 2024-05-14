class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for i in range(len(grid) - 1):
            for j in range(len(grid[0]) - 1):
                if grid[i][j] != grid[i + 1][j]:
                    return False
                if grid[i][j] == grid[i][j + 1]:
                    return False
        
        a = len(grid[0]) - 1
        for i in range(len(grid) - 1):
            if grid[i][a] != grid[i + 1][a]:
                return False
        a = len(grid) - 1
        for i in range(len(grid[0]) - 1):
            if grid[a][i] == grid[a][i + 1]:
                return False
        return True
