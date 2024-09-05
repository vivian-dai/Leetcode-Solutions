class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (len(rolls) + n)
        total -= sum(rolls)
        avg = total // n
        if avg < 1 or avg > 6 or (avg == 6 and n * 6 < total):
            return []
        missing = [avg] * n
        total -= (avg * n)
        idx = 0
        while total > 0:
            missing[idx] += 1
            total -= 1
            idx += 1
            idx %= n
        return missing
