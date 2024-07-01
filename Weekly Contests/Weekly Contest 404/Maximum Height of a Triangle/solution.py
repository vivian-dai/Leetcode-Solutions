class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        r = 0
        b = 0
        current = 0
        while True:
            if current % 2 == 0:
                r += current
                if max(red, blue) < r or min(red, blue) < b:
                    break
            else:
                b += current
                if max(red, blue) < b or min(red, blue) < r:
                    break
            current += 1
        return current - 1
