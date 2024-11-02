# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        elements=[]
        curr=head
        while curr:
            elements.append(curr)
            if curr.next:
                curr=curr.next
            else:
                break
        a=elements[left-1:right]
        a.reverse()
        for i in range(0,left-1):
            a.insert(i,elements[i])
        a.extend(elements[right:])
        curr=a[0]
        for i in range(1,len(a)):
            curr.next=a[i]
            curr=curr.next
        curr.next=None
        return a[0]

