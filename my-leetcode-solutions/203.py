# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ele=[]
        curr=head
        while curr:
            ele.append(curr)
            if curr.next:
                curr=curr.next
            else:
                break
        i=0
        while i<len(ele):
            if ele[i].val==val:
                ele.pop(i)
            else:
                i+=1
        if len(ele)==0:
            return None
        curr=ele[0]
        for i in range(1,len(ele)):
            curr.next=ele[i]
            curr=curr.next
        curr.next=None
        return ele[0]
