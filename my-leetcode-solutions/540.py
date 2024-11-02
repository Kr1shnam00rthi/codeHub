class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l=0
        e=len(nums)-1
        while l<=e:
            if nums[l]==nums[l+1]:
                l+=2
            else:
                return nums[l]
            if nums[e]==nums[e-1]:
                e-=2
            else:
                return nums[e]
        
