class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        for c in s:
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
                vowels.append(c)
        vowels.sort()
        point = 0
        s = list(s)
        for i in range(len(s)):
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
                s[i] = vowels[point]
                point += 1
        return ''.join(s)
