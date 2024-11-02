class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1=[s[i] for i in range(len(s))]
        l2=[t[i] for i in range(len(t))]
        if len(l1)>len(l2):
            l1,l2=l2,l1
        for x in l1:
            if x in l2:
                l2.remove(x)
        return len(l2)==0
