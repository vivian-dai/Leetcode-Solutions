# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def find_depth(tree):
            if tree == None:
                return 0
            elif tree.left is not None and tree.right is not None:
                return min(find_depth(tree.left), find_depth(tree.right)) + 1
            elif tree.left is None:
                return find_depth(tree.right) + 1
            else:
                return find_depth(tree.left) + 1
            
        return find_depth(root)
        