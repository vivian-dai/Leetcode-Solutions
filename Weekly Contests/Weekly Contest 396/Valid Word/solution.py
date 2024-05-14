class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False # length less than 3
        if not word.isalnum():
            return False # not all alphanumeric
        vow = False
        con = False
        vowels = "AEIOUaeiou"
        for c in word:
            if c.isnumeric():
                continue
            elif c in vowels:
                vow = True
            else:
                con = True
        return vow and con
