class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        while len(operations)!=0:
            t=operations.pop(0)
            if t=='C' and len(stack)!=0:
                stack.pop()
            elif t=='D' and len(stack)!=0:
                stack.append(int(stack[-1])*2)
            elif t=='+' and len(stack)>=2:
                stack.append(int(stack[-1])+int(stack[-2]))
            else:
                stack.append(int(t))
        return sum(stack)
