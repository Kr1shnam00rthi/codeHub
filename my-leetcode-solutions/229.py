class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        s=set(nums)
        res=[]
        n=len(nums)//3
        for x in s:
            c=nums.count(x)
            if c>n:
                res.append(x)
        return res
