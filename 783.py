# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        vals=[]
        def preorder(node,vals):
            if not node:
                return vals
            vals.append(node.val)
            vals=preorder(node.left,vals)
            vals=preorder(node.right,vals)
            return vals
        vals=preorder(root,vals)
        vals.sort()
        res=[]
        start=vals[0]
        for i in range(1,len(vals)):
            res.append(abs(vals[i]-start))
            start=vals[i]
        return min(res)
