class Solution:
    def makeGood(self, s: str) -> str:
        stack=[s[0]]
        for i in range(1,len(s)):
            stack.append(s[i])
            while len(stack)>1:
                a=stack[-1]
                b=stack[-2]
                if ((a.islower() and b.isupper() and a==b.lower()) or (a.isupper() and b.islower() and a==b.upper() )):
                    stack.pop()
                    stack.pop()
                else:
                    break 
        res=""
        for x in stack:
            res+=x
        return res
