class Solution:
    def tribonacci(self, n: int) -> int:
        tabs = {0:0, 1:1, 2:1} # list of tribonacci numbers
        def tri(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            elif n == 2:
                return 1
            elif n in tabs:
                return tabs[n]
            else:
                trin1 = 0
                trin2 = 0
                trin3 = 0
                trin = 0
                if (n - 1) in tabs:
                    trin1 = tabs[n - 1]
                else:
                    trin1 = tri(n - 1)
                    tabs[n - 1] = trin1
                if (n - 2) in tabs:
                    trin2 = tabs[n - 2]
                else:
                    trin2 = tri(n - 2)
                    tabs[n - 2] = trin2
                if (n - 3) in tabs:
                    trin3 = tabs[n - 3]
                else:
                    trin3 = tri(n - 3)
                    tabs[n - 3] = trin3
            trin = trin1 + trin2 + trin3
            return trin
        return tri(n)
        