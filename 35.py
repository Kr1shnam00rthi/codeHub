class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            if nums[0]>=target:
                return 0
            return 1
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            elif nums[i]>target:
                return i
        return len(nums) 
