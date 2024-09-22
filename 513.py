# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        elements=[]
        queue=[root]
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
            elements.extend([t])
        x=elements[-1]
        return x[0]
