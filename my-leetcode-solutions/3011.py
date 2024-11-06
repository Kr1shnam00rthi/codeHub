class Solution:
    def calbit(self,num):
        num=str(bin(num))[2:]
        return (num.count('1'))

    def canSortArray(self, nums: List[int]) -> bool:
        num=nums.copy()
        num.sort()
        for i in range(len(nums)):
            for j in range(0,len(nums)-i-1):
                if nums[j]>nums[j+1] and self.calbit(nums[j])==self.calbit(nums[j+1]):
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return num==nums
