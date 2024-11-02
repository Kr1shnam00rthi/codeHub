# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def check_odd(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:  
                return False
            if nums[i] % 2 == 0 or nums[i + 1] % 2 == 0: 
                return False
        return True

    def check_even(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:  # Ensure strictly decreasing order
                return False
            if nums[i] % 2 != 0 or nums[i + 1] % 2 != 0:  # Ensure even values
                return False
        return True

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = [root]
        level = 0

        while queue:
            t = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                t.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level % 2 == 0:
                if not all(x % 2 == 1 for x in t) or not self.check_odd(t):
                    return False
            else:
                if not all(x % 2 == 0 for x in t) or not self.check_even(t):
                    return False

            level += 1
        return True

