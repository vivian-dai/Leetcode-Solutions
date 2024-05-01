class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = 0
        sum2 = 0
        for i in range(len(nums1)):
            sum1 += nums1[i]
            sum2 += nums2[i]
        return (sum2 - sum1) // len(nums1)
