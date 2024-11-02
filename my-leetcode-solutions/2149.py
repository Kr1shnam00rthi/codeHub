class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for x in nums:
            if x>=0:
                pos.append(x)
            else:
                neg.append(x)
        res=[]
        j=0
        k=0
        for i in range(len(nums)):
            if i%2==0:
                res.append(pos[j])
                j+=1
            else:
                res.append(neg[k])
                k+=1
        return res
