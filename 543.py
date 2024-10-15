# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def cal_depth(self,node):
        if not node:
            return 0
        d=1
        queue=[node]
        while len(queue)!=0:
            l=len(queue)
            for _ in range(l):
                n=queue.pop(0)
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            if len(queue)!=0:
                d+=1
        return d

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res=[]
        def preorder(node,res):
            if not node:
                return res
            res.append(self.cal_depth(node.left)+self.cal_depth(node.right))
            preorder(node.left,res)
            preorder(node.right,res)
            return res
        res=preorder(root,res)
        return max(res)

        
