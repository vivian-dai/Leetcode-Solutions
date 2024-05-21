# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root == None:
            return None
        left = self.removeLeafNodes(root.left, target)
        right = self.removeLeafNodes(root.right, target)
        if left == None and right == None and root.val == target:
            return None
        return TreeNode(root.val, left, right)
