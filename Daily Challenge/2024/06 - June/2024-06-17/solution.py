class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        ret = False
        a = 0
        while a * a <= c:
            b2 = c - (a * a)
            b = int(sqrt(b2))
            if b*b == b2:
                ret = True
                break
            a += 1
        return ret
