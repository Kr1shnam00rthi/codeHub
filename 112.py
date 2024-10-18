# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def preorder(node,nums,num):
            num+=node.val
            if not node.left and not node.right:
                nums.append(num)
                num-=node.val
                return nums,num
            if node.left:
                nums,num=preorder(node.left,nums,num)
            if node.right:
                nums,num=preorder(node.right,nums,num)
            num-=node.val
            return nums,num
        nums=[]
        num=0
        nums,num=preorder(root,nums,num)
