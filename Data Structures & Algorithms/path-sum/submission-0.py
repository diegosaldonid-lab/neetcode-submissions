# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path = []
        ret = [False]
        def backtrack(root,targetSum, path, ret):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right and sum(path) == targetSum:
                ret[0] = True
                return
            backtrack(root.left,targetSum,path,ret)
            backtrack(root.right,targetSum,path,ret)
            
            path.pop()
            return

        backtrack(root,targetSum,path,ret)
        return ret[0]
        