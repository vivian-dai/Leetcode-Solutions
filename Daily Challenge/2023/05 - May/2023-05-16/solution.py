# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:  # noqa: F821
        arr = [] # hahahaha imagine dealing with this as a linked list haha funny haha
        cur_node = head
        while cur_node:
            arr.append(cur_node.val)
            cur_node = cur_node.next
        n = len(arr)
        max = arr[0] + arr[n - 1]
        for i in range(1, int(n/2) + 1, 1):
            sum = arr[i] + arr[n - 1 - i]
            if sum > max:
                max = sum
        return max