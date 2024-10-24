class Solution:
    def largestGoodInteger(self, num: str) -> str:
        j=1
        res=[]
        l=len(num)
        while j<l-1:
            if num[j-1]==num[j] and num[j]==num[j+1]:
                res.append(num[j]+num[j]+num[j])
            j+=1
        ans=""
        for x in res:
            if x>ans:
                ans=x
        return ans
        

