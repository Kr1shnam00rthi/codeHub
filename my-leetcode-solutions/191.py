class Solution:
    def hammingWeight(self, n: int) -> int:
        res=str(bin(n))
        count=0
        for i in range(0,len(res)):
            if res[i]=="1":
                count+=1
        return count
        
