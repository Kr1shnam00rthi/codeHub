class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        elements=[i for i in range(0,n+1)]
        for x in elements:
            if x not in nums:
                return x
