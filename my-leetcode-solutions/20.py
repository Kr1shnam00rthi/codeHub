class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        stack.append(s[0])
        for i in range(1,len(s)):
            if s[i]==')':
                if len(stack)!=0 and stack[-1]=='(':
                    stack.pop()
                else:
                    return 0
            elif s[i]==']':
                if len(stack)!=0 and stack[-1]=='[':
                    stack.pop()
                else:
                    return 0
            elif s[i]=='}':
                if len(stack)!=0 and stack[-1]=='{':
                    stack.pop()
                else:
                    return 0
            else:
                stack.append(s[i])
        if len(stack)==0:
            return 1
        return 0
