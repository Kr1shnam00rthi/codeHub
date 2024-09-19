# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        elements=[]
        curr=head
        l=k
        temp=[]
        while curr:
            l-=1
            temp.append(curr.val)
            if l==0:
                temp.reverse()
                elements.extend(temp)
                l=k
                print(l)
                temp=[]
            if curr.next:
                curr=curr.next
            else:
                elements.extend(temp)
                break
        curr1=head
        for i in range(len(elements)):
            curr1.val=elements[i]
            curr1=curr1.next
        return head

