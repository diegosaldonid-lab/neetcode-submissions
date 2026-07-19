# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        o = []

        def traverse(root,o):
            if root is None:
                return

            traverse(root.left,o)
            o.append(root.val)
            traverse(root.right,o)
            return

        traverse(root,o)

        return o[k-1]