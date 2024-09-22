class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        elif len(nums)==2:
            if nums[0]>nums[1]:
                return 0
            return 1
        else:
            l=1
            e=len(nums)-2
            while l<=e:
                if nums[l]>nums[l+1] and nums[l]>nums[l-1]:
                    return l
                if nums[e]>nums[e+1] and nums[e]>nums[e-1]:
                    return e
                l+=1
                e-=1
        
        if nums[-1]>nums[-2]:
            return len(nums)-1
        return 0
