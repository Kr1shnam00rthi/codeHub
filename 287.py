class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num=nums.copy()
        num.sort()
        start=num[0]
        for i in range(1,len(nums)):
            if start==num[i]:
                return start
            else:
                start=num[i]
