# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res=[]
        queue=[root]
        while len(queue)!=0:
            l=len(queue)
            temp=[]
            for i in range(l):
                n=queue.pop(0)
                temp.append(n.val)
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            res.append(max(temp))
        return res
