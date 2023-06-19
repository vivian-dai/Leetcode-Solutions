class Solution:
    def isFascinating(self, n: int) -> bool:
        doub = n*2
        trip = n*3
        s = str(n) + str(doub) + str(trip)
        all_nums = []
        for i in range(10):
            all_nums.append(0)
        for c in s:
            all_nums[ord(c) - ord('0')] += 1
        return (all_nums[0] == 0) and (all_nums[1] == 1) and (all_nums[2] == 1) and (all_nums[3] == 1) and (all_nums[4] == 1) and (all_nums[5] == 1) and (all_nums[6] == 1) and (all_nums[7] == 1) and (all_nums[8] == 1) and (all_nums[9] == 1)