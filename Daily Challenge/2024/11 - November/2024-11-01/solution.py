class Solution:
    def makeFancyString(self, s: str) -> str:
        ret = []
        rep = 0
        last = None
        for c in s:
            if c == last:
                rep += 1
            else:
                rep = 1
            last = c
            if rep < 3:
                ret.append(c)
        return "".join(ret)