class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = -1
        for i in range(len(word)):
            if word[i] == ch:
                index = i
                break

        if index == -1:
            return word
        
        new_word = []
        for i in range(index, -1, -1):
            new_word.append(word[i])
        for i in range(index + 1, len(word)):
            new_word.append(word[i])
        return "".join(new_word)
