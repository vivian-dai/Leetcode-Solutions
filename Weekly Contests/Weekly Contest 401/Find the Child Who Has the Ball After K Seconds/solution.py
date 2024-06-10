class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        # simulation because math is ahrd
        
        pointer = 0
        dir = 1
        for i in range(k):
            pointer += dir
            if pointer == n - 1:
                dir = -1
            elif pointer == 0:
                dir = 1
        return pointer
