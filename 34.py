class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[-1,-1]
        if len(nums)==0:
            return res
        elif len(nums)==1 and nums[0]==target:
            return [0,0]
        else:
            l=0
            e=len(nums)-1
            while l!=len(nums):
                if nums[l]==target and res[0]==-1:
                    res[0]=l
                if nums[e]==target and res[1]==-1:
                    res[1]=e
                l+=1
                e-=1
                if res[0]!=-1 and res[1]!=-1:
                    break
        return res
