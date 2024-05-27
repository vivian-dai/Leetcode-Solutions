class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        last = word[0]
        count = 0
        for c in word:
            if c != last or count == 9:
                comp += str(count)
                comp += str(last)
                last = c
                count = 1
            else:
                count += 1
        comp += str(count)
        comp += str(last)
        return comp
