class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_counter = 0
        for num in arr:
            if num % 2 == 1:
                odd_counter += 1
            else:
                odd_counter = 0
            if odd_counter == 3:
                return True
        return False
