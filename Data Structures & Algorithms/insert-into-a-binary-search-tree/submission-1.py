# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if not root:
            return node

        def insert(root,node):
            if not root:
                return
            
            if node.val > root.val:
                if not root.right:
                    root.right = node
                else:
                    insert(root.right,node)
            if node.val < root.val:
                if not root.left:
                    root.left = node
                else:
                    insert(root.left,node)
            return root
        
        return insert(root,node)
