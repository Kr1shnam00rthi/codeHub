# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals=[]
        curr=head
        while curr:
            vals.append(curr.val)
            curr=curr.next
        vals.reverse()
        m=vals[0]
        res=[]
        res.append(m)
        for i in range(1,len(vals)):
            if vals[i]>=m:
                m=vals[i]
                res.append(m)
        res.reverse()
        curr=ListNode(res[0])
        s=curr
        for i in range(1,len(res)):
            curr.next=ListNode(res[i])
            curr=curr.next
        return s 
