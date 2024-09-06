# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s=set()
        curr=head
        while curr:
            if curr in s:
                return True
            else:
                s.add(curr)
                if curr.next:
                    curr=curr.next
                else:
                    break
        return False
