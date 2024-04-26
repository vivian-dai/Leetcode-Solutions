class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lol = [0]* 10001
        for num in nums:
            lol[abs(num)] += 1
        ret = []
        for i in range(len(lol)):
            for j in range(lol[i]):
                ret.append(i*i)
        return ret
