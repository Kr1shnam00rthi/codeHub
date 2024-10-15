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
            for i in range(len(queue)):
                n=queue.pop(0)
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            if len(queue)!=0:
                d+=1
        return d
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 1
        c=1
        def preorder(node,c):
            d1=self.cal_depth(node.left)
            d2=self.cal_depth(node.right)
            print(d1,d2)
            if d1>d2:
                if (d1-d2)>1:
                    c=0
                    return c
            elif (d2-d1)>1:
                c=0
                return c
            if node.left:
                c=preorder(node.left,c)
            if node.right:
                c=preorder(node.right,c)
            return c
        c=preorder(root,c)
        print(c)
        return c

        
         
