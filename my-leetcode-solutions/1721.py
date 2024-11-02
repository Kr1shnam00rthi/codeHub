# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ele=[]
        curr=head
        while curr:
            ele.append(curr)
            if curr.next:
                curr=curr.next
            else:
                break
        ele[k-1],ele[-k]=ele[-k],ele[k-1]
        curr=ele[0]
        for i in range(len(ele)):
            curr.next=ele[i]
            curr=curr.next
        curr.next=None
        return ele[0]
