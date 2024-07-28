# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head.next # head is 0
        new_head = None
        last = None
        sum = 0
        while cur is not None:
            sum += cur.val
            cur = cur.next
            if cur.val == 0:
                if new_head == None:
                    new_head = ListNode(sum, None)
                    last = new_head
                else:
                    last.next = ListNode(sum, None)
                    last = last.next
                sum = 0
                cur = cur.next
        return new_head
