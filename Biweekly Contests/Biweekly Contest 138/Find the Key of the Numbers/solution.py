class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1_arr = []
        num2_arr = []
        num3_arr = []
        while num1 > 0:
            num1_arr.append(num1%10)
            num1 //= 10
        while len(num1_arr) < 4:
            num1_arr.append(0)
        num1_arr = num1_arr[::-1]
        while num2 > 0:
            num2_arr.append(num2%10)
            num2 //= 10
        while len(num2_arr) < 4:
            num2_arr.append(0)
        num2_arr = num2_arr[::-1]
        while num3 > 0:
            num3_arr.append(num3%10)
            num3 //= 10
        while len(num3_arr) < 4:
            num3_arr.append(0)
        num3_arr = num3_arr[::-1]
        ret = ""
        ret += str(min(num1_arr[0], num2_arr[0], num3_arr[0]))
        ret += str(min(num1_arr[1], num2_arr[1], num3_arr[1]))
        ret += str(min(num1_arr[2], num2_arr[2], num3_arr[2]))
        ret += str(min(num1_arr[3], num2_arr[3], num3_arr[3]))
        return int(ret)
        