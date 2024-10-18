# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def preorder(node,low,high,total):
            if not node:
                return total
            if node.val>=low and node.val<=high:
                total+=node.val
            total=preorder(node.left,low,high,total)
            total=preorder(node.right,low,high,total)
            return total
        return preorder(root,low,high,0)
