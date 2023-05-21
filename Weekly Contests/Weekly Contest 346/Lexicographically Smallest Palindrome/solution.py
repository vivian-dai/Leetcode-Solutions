class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        # basically need to make the string a palindrome and
        # to do that, letters equally distant from the center
        # must match with each other. needs to be lexicographically 
        # least so need to set letters based on which is lower
        for i in range(int(len(s)/2)):
            if s[i] < s[len(s) - i - 1]:
                s[len(s) - i - 1] = s[i]
            else:
                s[i] = s[len(s) - i - 1]
        return "".join(s)