class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=[]
        if nums[0]!=nums[1]:
            res.append(nums[0])
        if nums[-1]!=nums[-2]:
            res.append(nums[-1])
        for i in range(1,len(nums)-1):
            if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                res.append(nums[i])
        return res
