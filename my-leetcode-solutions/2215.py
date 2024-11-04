class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans=[]
        t1=[]
        t2=[]
        for x in nums1:
            if x not in nums2 and x not in t1:
                t1.append(x)
        for y in nums2:
            if y not in nums1 and y not in t2:
                t2.append(y)
        ans.append(t1)
        ans.append(t2)
        return ans
