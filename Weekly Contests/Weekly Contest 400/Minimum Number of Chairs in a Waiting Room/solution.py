class Solution:
    def minimumChairs(self, s: str) -> int:
        current = 0
        maxim = 0
        for c in s:
            if c == 'E':
                current += 1
            elif c == 'L':
                current -= 1
            maxim = max(maxim, current)
        return maxim
