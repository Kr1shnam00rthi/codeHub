class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        res=0
        for x in nums:
            if x-1 not in num:
                length=0
                while (x+length) in num:
                    length+=1
                res=max(res,length)                
        return res
