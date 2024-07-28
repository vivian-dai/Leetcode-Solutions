class Solution:
    def minChanges(self, n: int, k: int) -> int:
        n = "{0:b}".format(n)
        k = "{0:b}".format(k)
        n = n.rjust(max(len(n), len(k)), "0")
        k = k.rjust(max(len(n), len(k)), "0")
        counter = 0
        for i in range(len(n)):
            if n[i] != k[i]:
                if n[i] == "0":
                    return -1
                counter += 1
        return counter
