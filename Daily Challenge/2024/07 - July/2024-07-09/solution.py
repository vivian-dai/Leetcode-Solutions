class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_time = 0
        cur_time = customers[0][0]
        for customer in customers:
            cur_time = max(cur_time, customer[0])
            cur_time += customer[1]
            total_time += (cur_time - customer[0])
        return total_time / len(customers)
