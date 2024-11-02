class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele=set(nums)
        m=0
        c=0
        for x in ele:
            t=nums.count(x)
            if t>c:
                m=x
                c=t
        return m
