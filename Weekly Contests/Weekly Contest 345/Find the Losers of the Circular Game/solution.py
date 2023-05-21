class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:  # noqa: F821
        received = [False for i in range(n)]
        steps = k
        received[0] = True
        ind = 0
        while 1:
            ind += steps
            ind %= n
            if received[ind]:
                break
            received[ind] = True
            steps += k
        losers = []
        for i in range(n):
            if not received[i]:
                losers.append(i + 1)
        return losers