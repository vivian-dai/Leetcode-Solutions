class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        inc = True
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                # this is fine if inc is true
                if not inc:
                    return False
            elif arr[i] < arr[i - 1]:
                if i == 1:
                    return False
                if inc:
                    inc = False
            else:
                return False
        if inc:
            return False
        return True
