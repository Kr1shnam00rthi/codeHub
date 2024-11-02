class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res=[0 for i in range(2*len(nums))]
        l=len(nums)
        for i in range(l):
            res[i]=nums[i]
            res[i+l]=nums[i]
        return res
