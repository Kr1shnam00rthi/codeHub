class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        nums.sort()
        start=nums[0]
        for i in range(1,len(nums)):
            if start==nums[i]:
                res.append(start)
            start=nums[i]
        return res
