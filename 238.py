class Solution:
    def calproduct(self,nums):
        pro=1
        l=0
        e=len(nums)-1
        while l<=e:
            if l==e:
                pro*=nums[e]
                return pro
            pro*=nums[e]
            pro*=nums[l]
            e-=1
            l+=1
        return pro
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        if 0 not in nums:
            pro=1
            l=0
            e=len(nums)-1
            while l<=e:
                if l==e:
                    pro*=nums[e]
                    break
                pro*=nums[e]
                pro*=nums[l]
                l+=1
                e-=1
            for x in nums:
                res.append(pro//x)
            return res
        for i in range(len(nums)):
            num=nums.copy()
            num.pop(i)
            if 0 in num:
                res.append(0)
            else:
                res.append(self.calproduct(num))
        return res
