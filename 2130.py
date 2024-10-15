# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        val=[]
        curr=head
        while curr:
            val.append(curr.val)
            curr=curr.next
        res=0
        for i in range(len(val)//2):
            if (val[i]+val[-1-i])>res:
                res=(val[i]+val[-1-i])
        return res
