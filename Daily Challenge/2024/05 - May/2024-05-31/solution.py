class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ret = []
        # two passes, first to add, second to remove for each number
        for num in nums:
            if num in ret:
                ret.remove(num)
            else:
                ret.append(num)
        return ret
