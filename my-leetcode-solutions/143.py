# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        elements=[]
        curr=head
        while curr:
            elements.append(curr)
            if curr.next:
                curr=curr.next
            else:
                break
        res=[]
        for i in range(int(len(elements)/2)):
            res.append(elements[i])
            res.append(elements[-i-1])
        if len(elements)%2!=0:
            res.append(elements[int(len(elements)/2)])
        head=res[0]
        curr=head
        for i in range(1,len(res)):
            curr.next=res[i]
            curr=res[i]
        curr.next=None
        return head
