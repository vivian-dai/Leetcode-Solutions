# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:  # noqa: F821

        def make_list(root):
            if root.val == None:
                return []
            elif root.left == None and root.right == None:
                return [root.val]
            elif root.left == None:
                return [root.val] + make_list(root.right)
            elif root.right == None:
                return [root.val] + make_list(root.left)
            else:
                return [root.val] + make_list(root.left) + make_list(root.right)
            
        lst = make_list(root)
        lst.sort()
        min_diff = lst[1] - lst[0]
        for i in range(2, len(lst)):
            diff = lst[i] - lst[i - 1]
            if diff < min_diff:
                min_diff = diff
        
        return min_diff
        