# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        new_head = None
        while(current_node):
            new_node = ListNode(current_node.val, new_head)
            new_head = new_node
            current_node = current_node.next
        return new_head
        