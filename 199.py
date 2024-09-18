# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue=[]
        res=[]
        queue.append(root)
        while True:
            l=len(queue)
            temp=[]
            for i in range(len(queue)):
                element=queue.pop(0)
                temp.append(element.val)
                if element.right:
                    queue.append(element.right)
                if element.left:
                    queue.append(element.left)
            res.append(temp[0])
            if len(queue)==0:
                break
        return res
