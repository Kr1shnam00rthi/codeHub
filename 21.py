# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        curr=list1
        while curr:
            if curr.next:
                curr=curr.next
            else:
                break
        if not curr:
            return list2
        curr.next=list2
        ele=[]
        curr=list1
        while curr:
            ele.append(curr)
            if curr.next:
                curr=curr.next
            else:
                break
        for i in range(0,len(ele)):
            for j in range(0,len(ele)-i-1):
                if ele[j].val>ele[j+1].val:
                    ele[j].val,ele[j+1].val=ele[j+1].val,ele[j].val
        for i in range(len(ele)-1):
            ele[i].next=ele[i+1]
        return ele[0]


