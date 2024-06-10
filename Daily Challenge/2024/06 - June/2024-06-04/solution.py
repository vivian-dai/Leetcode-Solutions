class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = [0] * 128 # just ascii, don't really care
        for c in s:
            letters[ord(c)] += 1
        
        # now we count all the even ones
        counter = 0
        has_one = False
        for num in letters:
            if num % 2 == 0:
                counter += num
            else:
                counter += num - 1
                has_one = True
        return counter + (1 if has_one else 0)
