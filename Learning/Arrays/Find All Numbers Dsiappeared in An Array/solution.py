class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret = []
        n = len(nums)
        counter = [0] * n
        for num in nums:
            counter[num - 1] += 1
        for i in range(len(counter)):
            if counter[i] == 0:
                ret.append(i + 1)
        return ret
