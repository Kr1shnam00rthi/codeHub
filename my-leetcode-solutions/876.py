# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        ele=[]
        curr=head
        while curr:
            ele.append(curr)
            if curr.next:
                curr=curr.next
            else:
                break
        print(len(ele))
        i=0
        while i<len(ele)-1:
            if ele[i].val==ele[i+1].val:
                ele.pop(i)
            else:
                i+=1
        curr=ele[0]
        for i in range(1,len(ele)):
            curr.next=ele[i]
            curr=curr.next
        curr.next=None
        return ele[0]
        
