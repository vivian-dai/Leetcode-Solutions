class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        has = []
        def has_all(arr: List[bool]) -> bool:
            for a in arr:
                if not a:
                    return False
            return True
        for i in range(k):
            has.append(False)
        nums.reverse()
        operations = 1
        for num in nums:
            if num <= k:
                has[num - 1] = True
                if has_all(has): 
                    return operations
            operations += 1
        return -1
