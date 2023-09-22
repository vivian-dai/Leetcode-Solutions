class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        def is_sorted(li: List[int]) -> bool:
            last = li[0]
            for i in range(1, len(li)):
                if last > li[i]:
                    return False
                last = li[i]
            return True
        for i in range(len(nums)):
            if(is_sorted(nums)):
                return i
            nums.insert(0, nums[-1])
            nums = nums[:-1]
        return -1
        