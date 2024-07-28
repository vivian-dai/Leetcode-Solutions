from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # find top left and bottom right then do math
        top = None
        left = None
        bottom = None
        right = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if top == None: # first time seeing a 1
                        top = i
                        left = j
                        bottom = i + 1
                        right = j + 1
                    else:
                        if i < top:
                            top = i
                        if i + 1 > bottom:
                            bottom = i + 1
                        if j < left:
                            left = j
                        if j + 1 > right:
                            right = j + 1
        return (bottom - top) * (right - left)
