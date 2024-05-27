class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums) + 1):
            # see if x=i
            counter = 0
            for num in nums:
                if num >= i:
                    counter += 1
            if counter == i:
                return i
        return -1
