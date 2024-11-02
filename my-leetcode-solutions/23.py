# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            if not lists:
                return None
            elements=[]
            for x in lists:
                curr=x
                while curr:
                    elements.append(curr.val)
                    if curr.next:
                        curr=curr.next
                    else:
                        break
            if len(elements)==0:
                return None
            elements.sort()
            print(elements)
            n=ListNode(elements[0])
            start=n
            for i in range(1,len(elements)):
                n.next=ListNode(elements[i])
                n=n.next
            return start
