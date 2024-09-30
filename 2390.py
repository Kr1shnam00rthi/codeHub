class Solution:
    def removeStars(self, s: str) -> str:
        r=[]
        i=0
        while i<len(s):
            if s[i]!="*":
                r.append(s[i])
            else:
                if len(r)!=0:
                    r.pop()
            i+=1
        res=""
        for x in r:
            res+=x
        return res
