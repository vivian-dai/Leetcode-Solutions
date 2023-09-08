class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1] == 1:
            return 0
        result = []
        for i in range(len(obstacleGrid)):
            line = []
            for j in range(len(obstacleGrid[0])):
                line.append(0)
            result.append(line)
        
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                break
            result[i][0] = 1
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1:
                break
            result[0][i] = 1
        
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 0:
                    result[i][j] = result[i - 1][j] + result[i][j - 1]
        print(result)
        return result[len(result) - 1][len(result[0]) - 1]
