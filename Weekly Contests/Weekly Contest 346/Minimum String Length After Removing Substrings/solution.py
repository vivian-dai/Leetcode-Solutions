class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if ("AB" in s) and ("CD" in s):
        #     # return min
        #     return min(self.minLength("".join(s.split("AB"))), self.minLength("".join(s.split("CD"))))
        # elif "AB" in s:
        #     return self.minLength("".join(s.split("AB")))
        if "AB" in s:
            return self.minLength("".join(s.split("AB")))
        elif "CD" in s:
            return self.minLength("".join(s.split("CD")))
        else:
            return len(s)
        # the comments show this problem was overcomplicated more than it should've been in my head