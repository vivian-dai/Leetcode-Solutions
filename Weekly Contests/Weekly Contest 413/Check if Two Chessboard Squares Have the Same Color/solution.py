class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        coord1 = int(coordinate1[1]) + (ord(coordinate1[0]) - ord('a') + 1)
        coord2 = int(coordinate2[1]) + (ord(coordinate2[0]) - ord('a') + 1)
        return coord1%2 == coord2%2
