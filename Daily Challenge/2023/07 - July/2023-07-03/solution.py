class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        i1 = None
        i2 = None
        dups = []
        for i in range(26):
            dups.append(0)
        for i in range(len(s)):
            dups[ord(s[i]) - ord('a')] += 1
            if s[i] != goal[i]:
                # indexes are different, 3 cases
                if i1 == None:
                    i1 = i
                elif i2 == None:
                    i2 = i
                else:
                    return False
        
        if i1 == None and i2 == None:
            for num in dups:
                if num >= 2:
                    return True
            return False
        elif i2 == None:
            return False
        else:
            return s[i1] == goal[i2] and s[i2] == goal[i1]
