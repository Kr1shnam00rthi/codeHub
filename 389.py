class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=[s[i] for i in range(len(s))]
        t=[t[i] for i in range(len(t))]
        l=0
        e=len(t)-1
        while l<=e:
            if t[l] not in s:
                return t[l]
            else:
                s.remove(t[l])
            if t[e] not in s:
                return t[e]
            else:
                s.remove(t[e])
            l+=1
            e-=1

