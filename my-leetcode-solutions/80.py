class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c=1
        start=nums[0]
        i=1
        while(i<len(nums)):
            if nums[i]!=start:
                start=nums[i]
                c=1
                i+=1
            elif nums[i]==start:
                if c<2:
                    c+=1
                    i+=1
                else:
                    nums.pop(i)
        return len(nums)
