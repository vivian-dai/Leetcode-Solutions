"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ret = []

        def recurse(node):
            if node == None: return
            for child in node.children:
                recurse(child)
            ret.append(node.val)

        recurse(root)
        return ret
