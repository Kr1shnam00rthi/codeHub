# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1=[]
        stack2=[]
        curr1=l1
        curr2=l2
        while curr1:
            stack1.append(curr1.val)
            if curr1.next:
                curr1=curr1.next
            else:
                break
        while curr2:
            stack2.append(curr2.val)
            if curr2.next:
                curr2=curr2.next
            else:
                break
        if len(stack1)<len(stack2):
            stack1,stack2=stack2,stack1
        c=0
        for i in range(len(stack2)):
            a=stack1[i]+stack2[i]+c
            if a>=10:
                c=a//10
                stack1[i]=a%10
            else:
                c=0
                stack1[i]=a
        if c!=0:
            j=len(stack2)
            while j<len(stack1):
                a=stack1[j]+c
                if a>=10:
                    stack1[j]=a%10
                    c=a//10
                else:
                    c=0
                    stack1[j]=a
                j+=1
            if c!=0:
                stack1.append(c)
        n=ListNode(stack1[0])
        start=n
        for i in range(1,len(stack1)):
            n.next=ListNode(stack1[i])
            n=n.next
        return start
