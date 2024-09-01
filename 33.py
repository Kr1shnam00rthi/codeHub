class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        e=len(nums)-1
        while l<=e:
            if nums[l]==target:
                return l
            elif nums[e]==target:
                return e
            l+=1
            e-=1
        return -1
