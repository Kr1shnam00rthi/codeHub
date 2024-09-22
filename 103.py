# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[]
        queue=[root]
        c=0
        while len(queue)!=0:
            l=len(queue)
            t=[]
            for i in range(l):
                n=queue.pop(0)
                t.append(n.val)
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)    
            if c==0:
                res.extend([t])
                c=1
            else:
                t=t[::-1]
                res.extend([t])
                c=0
        return res
