# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0
        res=[]
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        a=res[0]
        for i in range(1,len(res)): 
            if res[i]>a:
                a=res[i]
            else:
                return 0
        return 1
