class Solution:
    def isincrease(self,nums):
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return False
        return True
    
    def isdecrease(self,nums):
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                return False
        return True
    def isMonotonic(self, nums: List[int]) -> bool:
        r1=self.isincrease(nums)
        r2=self.isdecrease(nums)
        if r1:
            return r1
        if r2:
            return r2
        return False

