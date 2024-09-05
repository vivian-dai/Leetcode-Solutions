class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        grid = []
        counter = 0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(counter)
                counter += 1
            grid.append(row)
        x, y = 0, 0
        for command in commands:
            if command == "RIGHT":
                x += 1
            elif command == "LEFT":
                x -=1
            elif command == "UP":
                y -=1
            elif command == "DOWN":
                y += 1
        return grid[y][x]
