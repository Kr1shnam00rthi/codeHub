# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,node,res):
        if not node:
            res.append("NULL")
            return res
        res.append(node.val)
        res=self.preorder(node.left,res)
        res=self.preorder(node.right,res)
        return res

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        sub=self.preorder(subRoot,[])   
        def level(node,sub):
            queue=[node]
            res=False
            while len(queue)!=0:
                l=len(queue)
                for i in range(l):  
                    n=queue.pop(0)
                    if sub==self.preorder(n,[]):
                        res=True
                        break
                    if n.left:
                        queue.append(n.left)
                    if n.right:
                        queue.append(n.right)
                if res:
                    break
            return res
        return level(root,sub)    
