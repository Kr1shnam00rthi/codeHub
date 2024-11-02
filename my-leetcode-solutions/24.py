# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        i=0
        while curr:
            if i%2==0 and curr.next:
                curr.val,curr.next.val=curr.next.val,curr.val
            if curr.next:
                curr=curr.next
            else:
                break
            i+=1
        return head
