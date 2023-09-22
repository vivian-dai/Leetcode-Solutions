class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        car = []
        for i in range(101):
            car.append(False)
        for num in nums:
            for j in range(num[0], num[1] + 1):
                car[j] = True
        count = 0
        for c in car:
            if c:
                count += 1
        return count
