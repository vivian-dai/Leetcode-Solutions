
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        
        if s1[0] == s2[2]:
            t = s1[0]
            s1[0] = s1[2]
            s1[2] = t
        if s1[1] == s2[3]:
            t = s1[1]
            s1[1] = s1[3]
            s1[3] = t
        if s1[3] == s2[1]:
            t = s1[3]
            s1[3] = s1[1]
            s1[1] = t
        if s1[2] == s2[0]:
            t = s1[2]
            s1[2] = s1[0]
            s1[0] = t

        return s1 == s2
