from typing import List

# ok nevermind this is a DP problem too much work
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        max = None
        n = len(energy)
        for i in range(n):
            sum = 0
            for j in range(i, n, k):
                sum += energy[j]
            if max == None:
                max = sum
            elif sum > max:
                max = sum
        return max
        
print(Solution().maximumEnergy([-2,-3,-1], 2))
