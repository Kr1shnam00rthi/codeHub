class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        for i in range(len(nums)):
            for j in range(0,len(nums)-i-1):
                if nums[j]==0:
                    nums[j],nums[j+1]=nums[j+1],nums[j]