# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=[]
        queue.append(root)
        res=[[]]
        while True:
            l=len(queue)
            temp=[]
            for i in range(l):
                element=queue.pop(0)
                temp.append(element.val)
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            res.extend([temp])
            if len(queue)==0:
                break
        return res[1:]
