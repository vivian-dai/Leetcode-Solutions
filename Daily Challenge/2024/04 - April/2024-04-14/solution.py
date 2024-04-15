# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRight(self, node):
        if node == None:
            return 0
        else:
            return self.sumLeft(node.left) + self.sumRight(node.right)
    def sumLeft(self, node) -> int:
        if node == None:
            return 0
        if node.left == None and node.right == None:
            # this leaf is a left leaf node
            return node.val
        else:
            return self.sumLeft(node.left) + self.sumRight(node.right)
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.sumLeft(root.left) + self.sumRight(root.right)
