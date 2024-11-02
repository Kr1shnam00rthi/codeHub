# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        elements=[]
        curr=head
        while curr:
            elements.append(curr)
            if not curr.next:
                break
            curr=curr.next
        elements.pop(len(elements)-n)
        if len(elements)==0:
            return None
        head=elements[0]
        curr=head
        for i in range(1,len(elements)):
            curr.next=elements[i]
            curr=elements[i]
        curr.next=None
        return head
