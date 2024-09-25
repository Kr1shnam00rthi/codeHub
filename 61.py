# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        l=0
        curr=head
        elements=[]
        while curr:
            l+=1
            elements.append(curr)
            if curr.next:
                curr=curr.next
            else:
                break
        k=k%l
        for i in range(k):
            t=elements.pop()
            elements.insert(0,t)
        curr=elements[0]
        for i in range(1,len(elements)):
            curr.next=elements[i]
            curr=elements[i]
        curr.next=None
        return elements[0]
        
