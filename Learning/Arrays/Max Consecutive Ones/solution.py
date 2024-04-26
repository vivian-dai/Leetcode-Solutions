class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        most = 0
        counter = 0
        for num in nums:
            if num == 1:
                counter += 1
            else:
                if counter > most:
                    most = counter
                counter = 0
        return max(most, counter)
