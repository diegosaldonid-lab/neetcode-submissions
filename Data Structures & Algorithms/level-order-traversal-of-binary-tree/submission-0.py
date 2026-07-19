# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = [[root]]
        ret = []

        while len(q):
            level = q.pop()
            c_level = []
            n_level = []
            for node in level:
                c_level.append(node.val)
                if node.left:
                    n_level.append(node.left)
                if node.right:
                    n_level.append(node.right)
            if len(n_level):
                q.append(n_level)
            ret.append(c_level)

        return ret
        