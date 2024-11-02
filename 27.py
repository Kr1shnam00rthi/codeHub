class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        e=len(nums)-1
        while l<=e:
            if l==e:
                if nums[l]==val:
                    nums[l]=101
            if nums[l]==val:
                nums[l]=101
            if nums[e]==val:
                nums[e]=101
            l+=1
            e-=1
        c=nums.count(101)
        nums.sort()
        return len(nums)-c
