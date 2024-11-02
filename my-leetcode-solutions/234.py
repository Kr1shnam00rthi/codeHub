# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ele=[]
        curr=head
        while curr:
            ele.append(curr.val)
            if curr.next:
                curr=curr.next
            else:
                break
        return ele==ele[::-1]
                
