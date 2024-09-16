class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        end = max(start, goal)
        start = min(start, goal)
        start = "{0:b}".format(start)[::-1]
        end = "{0:b}".format(end)[::-1]
        counter = 0
        for i in range(min(len(start), len(end))):
            if start[i] != end[i]:
                counter += 1
        for i in range(len(start), len(end)):
            if end[i] == "1":
                counter += 1
        return counter
