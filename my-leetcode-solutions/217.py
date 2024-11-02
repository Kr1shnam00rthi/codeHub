class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return False
        nums.sort()
        # Check with Two pointers
        l=0
        e=len(nums)-1
        while l<e:
            if nums[l]==nums[l+1]:1
                return True
            elif nums[e]==nums[e-1]:
                return True
            else:
                l+=1
                e-=1
        return False
