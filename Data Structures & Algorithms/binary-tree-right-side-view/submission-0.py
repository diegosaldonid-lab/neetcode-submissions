# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ret = []
        queue = [[root]]

        while queue:
            level = queue.pop()
            n_level = []
            for node in level:
                if node.left:
                    n_level.append(node.left)
                if node.right:
                    n_level.append(node.right)
            
            if len(n_level):
                queue.append(n_level)
            
            ret.append(node.val)

        return ret



        

        