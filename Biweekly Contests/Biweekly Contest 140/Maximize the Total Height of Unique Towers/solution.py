class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        totals = 0
        lastHeight = -1
        for mh in maximumHeight:
            if lastHeight == -1:
                totals += mh
                lastHeight = mh
            elif mh < lastHeight:
                totals += mh
                lastHeight = mh
            else:
                totals += (lastHeight - 1)
                lastHeight -= 1
                if lastHeight == 0:
                    return -1
        return totals
