class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rows_used = []
        cols_used = []
        rows = n
        cols = n
        sum = 0
        for i in range(n):
            rows_used.append(False)
            cols_used.append(False)
        for query in queries[::-1]:
            if query[0] == 0:
                if not rows_used[query[1]]:
                    rows_used[query[1]] = True
                    cols -= 1
                    sum += query[2]*rows
            elif query[0] == 1:
                if not cols_used[query[1]]:
                    cols_used[query[1]] = True
                    rows -= 1
                    sum += query[2]*cols
        return sum
