"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        queue=[root]
        while len(queue)!=0:
            for i in range(0,len(queue)-1):
                queue[i].next=queue[i+1]
            queue[-1].next=None
            l=len(queue)
            for i in range(l):
                n=queue.pop(0)
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
        return root
