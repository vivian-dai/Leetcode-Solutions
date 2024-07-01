class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        counter = [0] * (len(edges) + 1) # array of n
        for edge in edges:
            counter[edge[0] - 1] += 1
            counter[edge[1] - 1] += 1
        # find biggest
        largest_ind = 0
        for i in range(len(counter)):
            if counter[i] > counter[largest_ind]:
                largest_ind = i
        return largest_ind + 1
