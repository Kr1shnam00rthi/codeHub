# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrder(self,node):
        queue=[]
        queue.append(node)
        temp=[]
        temp.append(node.val)
        while len(queue)!=0:
            l=len(queue)
            if temp!=temp[::-1]:
                return False
            temp=[] 
            for i in range(l):
                n=queue.pop(0)
                if n.left:
                    queue.append(n.left)
                    temp.append(n.left.val)
                else:
                    temp.append("Null")
                if n.right:
                    queue.append(n.right)
                    temp.append(n.right.val)
                else:
                    temp.append("Null")
        return True
                
                
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.levelOrder(root)
