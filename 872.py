# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,node,ele):
        if not node.left and not node.right:
            ele.append(node.val)
            return ele
        if node.left:
            self.inorder(node.left,ele)
        if node.right:
            self.inorder(node.right,ele)
        return ele
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        ele1=[]
        ele2=[]
        ele1=self.inorder(root1,ele1)
        ele2=self.inorder(root2,ele2)
        return ele1==ele2
