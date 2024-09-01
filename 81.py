class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=0
        e=len(nums)-1
        while l<=e:
            if nums[l]==target:
                return 1
            elif nums[e]==target:
                return 1
            l+=1
            e-=1
        return 0
