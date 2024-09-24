class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(0,n+1):
            t=str(bin(i))
            count=0
            for i in range(0,len(t)):
                if t[i]=="1":
                    count+=1
            res.append(count)
        return res
