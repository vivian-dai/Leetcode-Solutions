class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            new_str = ""
            for letter in word:
                new_str += chr((((ord(letter) - ord('a')) + 1) % 26) + ord('a'))
            word += new_str
        return word[k - 1]
