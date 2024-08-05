class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        moves = [[0 for i in range(11)] for _ in range(n)]
        for p in pick:
            moves[p[0]][p[1]] += 1
        count = 0
        for i in range(len(moves)):
            most = 0
            for j in range(len(moves[i])):
                if moves[i][j] > most:
                    most = moves[i][j]
            if most > i: count += 1
        return count
