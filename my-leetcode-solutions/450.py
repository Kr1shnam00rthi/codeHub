# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        right_subtree = root.right
        last_right = self.find_last_right(root.left)
        last_right.right = right_subtree
        return root.left

    def find_last_right(self, root):
    
        if root.right is None:
            return root
        return self.find_last_right(root.right)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == key:

            return self.helper(root)
        parent = None
        curr = root
        while curr:
            if curr.val > key:
                if curr.left and curr.left.val == key:
                    curr.left = self.helper(curr.left)
                    break
                parent = curr
                curr = curr.left
            else:
                if curr.right and curr.right.val == key:
                    curr.right = self.helper(curr.right)
                    break
                parent = curr
                curr = curr.right
        
        return root

