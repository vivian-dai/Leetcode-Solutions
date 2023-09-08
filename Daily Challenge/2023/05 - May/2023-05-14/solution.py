# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:  # noqa: F821
        swapper_start = None
        swapper_end = None

        # find length
        length = 0
        cur_node = head
        while cur_node is not None:
            length += 1
            cur_node = cur_node.next

        # now we know indexes
        ind_start = k
        ind_end = length + 1 - k
        # print(ind_start, ind_end)
        
        # find values at those indexes
        cur_node = head
        index = 0
        while cur_node is not None:
            index += 1
            # print(swapper_start, swapper_end)
            if index == ind_start:
                swapper_start = cur_node.val
            if index == ind_end:
                swapper_end = cur_node.val
            cur_node = cur_node.next
        
        # swap
        index = 0
        cur_node = head
        while cur_node is not None:
            # print(index, ind_start)
            index += 1
            if index == ind_start:
                cur_node.val = swapper_end
                # print(cur_node)
            elif index == ind_end:
                cur_node.val = swapper_start
            cur_node = cur_node.next

        return head
