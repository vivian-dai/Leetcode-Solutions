# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def get_sum(node, cur_sum) -> int:
            if node:
                if not node.left and not node.right:
                    return cur_sum*10 + node.val
                return get_sum(node.left, cur_sum*10 + node.val) + get_sum(node.right, cur_sum*10 + node.val)
            return 0
        
        return get_sum(root, 0)
