# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ele=[]
        curr=head
        while curr:
            ele.append(curr)
            if curr.next:
                curr=curr.next
            else:
                break
        for i in range(len(ele)-1):
            j=i+1
            while j>0:
                if ele[j].val<ele[j-1].val:
                    ele[j].val,ele[j-1].val=ele[j-1].val,ele[j].val
                    j-=1
                else:
                    break
        curr=ele[0]
        for i in range(1,len(ele)):
            curr.next=ele[i]
            curr=curr.next
        return ele[0]
