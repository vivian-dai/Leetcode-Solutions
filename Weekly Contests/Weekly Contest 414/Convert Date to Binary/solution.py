class Solution:
    def convertDateToBinary(self, date: str) -> str:
        dates = date.split("-")
        return f"{bin(int(dates[0]))[2:]}-{bin(int(dates[1]))[2:]}-{bin(int(dates[2]))[2:]}"
