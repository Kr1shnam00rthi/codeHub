# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ele1=[]
        ele2=[]
        curr1=headA
        curr2=headB
        while curr1:
            ele1.append(curr1)
            if curr1.next:
                curr1=curr1.next
            else:
                break
        while curr2:
            ele2.append(curr2)
            if curr2.next:
                curr2=curr2.next
            else:
                break
        for x in ele1:
            if x in ele2:
                return x
        return None
