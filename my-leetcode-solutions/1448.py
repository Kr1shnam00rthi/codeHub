# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        nums=[]
        def preorder(node,nums,count):
            if len(nums)!=0 and node.val>=max(nums):
                count+=1
            nums.append(node.val)
            if node.left:
                nums,count=preorder(node.left,nums,count)
            if node.right:
                nums,count=preorder(node.right,nums,count)
            if len(nums)!=0:
                nums.pop()
            return nums,count
        
        nums,count=preorder(root,[],1)
        return count
