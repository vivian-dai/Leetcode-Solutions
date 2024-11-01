class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        output = []
        for num in nums:
            found = False
            for i in range(1, num):
                if i | (i + 1) == num:
                    found = True
                    output.append(i)
                    break
            if not found:
                output.append(-1)
        return output