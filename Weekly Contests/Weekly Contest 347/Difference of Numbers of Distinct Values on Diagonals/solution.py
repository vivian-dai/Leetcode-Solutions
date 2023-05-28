class Solution:
    def get_distinct_top_left(self, grid: List[List[int]], i, j, diff):  # noqa: F821
        if i < 0 or j < 0:
            return len(diff)
        else:
            diff.add(grid[i][j])
            return self.get_distinct_top_left(grid, i - 1, j - 1, diff)
        
    def get_distinct_bottom_right(self, grid: List[List[int]], i, j, diff):  # noqa: F821
        if i >= len(grid) or j >= len(grid[0]):
            return len(diff)
        else:
            diff.add(grid[i][j])
            return self.get_distinct_bottom_right(grid, i + 1, j + 1, diff)
        
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:  # noqa: F821
        arr = []
        for i in range(len(grid)):
            line = []
            for j in range(len(grid[0])):
                line.append(0)
            arr.append(line)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(i, j, self.get_distinct_bottom_right(grid, i + 1, j + 1, {*()}), self.get_distinct_top_left(grid, i - 1, j - 1, {*()}))
                arr[i][j] = abs(self.get_distinct_bottom_right(grid, i + 1, j + 1, {*()}) - self.get_distinct_top_left(grid, i - 1, j - 1, {*()}))
        return arr