# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        elements1 = []
        elements2 = []
        
        def inorder(node, elements):
            if not node:
                elements.append("0")
                return
            elements.append(node.val)
            inorder(node.left, elements)
            inorder(node.right, elements)
        
        
        inorder(p, elements1)
        inorder(q, elements2)
        
        return elements1 == elements2

