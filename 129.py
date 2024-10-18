# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def preorder(node,nums,num):
            num+=str(node.val)
            if not node.left and not node.right:
                nums.append(num)
                num=num[:len(num)-1]
                return nums,num
            if node.left:
                nums,num=preorder(node.left,nums,num)
            if node.right:
                nums,num=preorder(node.right,nums,num)
            num=num[:len(num)-1]
            return nums,num
        nums=[]
        num=""
        nums,num=preorder(root,nums,num)
        res=0
        for x in nums:
            res+=int(x)
        return res
