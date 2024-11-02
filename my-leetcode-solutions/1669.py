# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start=None
        end=None
        curr=list1
        while curr:
            if a==1:
                start=curr
            if b==-1:
                end=curr
            if curr.next:
                a-=1
                b-=1
                curr=curr.next
            else:
                break
        start.next=list2
        curr=list2
        while curr:
            if curr.next:
                curr=curr.next
            else:
                break
        curr.next=end
