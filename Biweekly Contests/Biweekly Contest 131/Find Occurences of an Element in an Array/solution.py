class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occs = []
        for i in range(len(nums)):
            if nums[i] == x:
                occs.append(i)
        output = []
        for q in queries:
            if q > len(occs):
                output.append(-1)
            else:
                output.append(occs[q - 1])
        return output
