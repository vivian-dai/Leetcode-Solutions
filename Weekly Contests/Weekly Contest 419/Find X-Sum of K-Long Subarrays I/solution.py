class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        answer = []
        for i in range(len(nums) - k + 1):
            sub = nums[i:min(len(nums), i + k)]
            freq = [0] * 51
            for s in sub:
                freq[s] += 1
            summ = 0
            for j in range(x):
                max_ind = 0
                for q in range(len(freq)):
                    if freq[q] >= freq[max_ind]:
                        max_ind = q
                summ += freq[max_ind] * max_ind
                freq[max_ind] = 0
            answer.append(summ)
        return answer
