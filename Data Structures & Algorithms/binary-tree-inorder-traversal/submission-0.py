# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []

        def traverse(root,ret):
            if not root:
                return
            
            traverse(root.left,ret)
            ret.append(root.val)
            traverse(root.right,ret)

            return
        
        traverse(root,ret)
        
        return ret
        