class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for x in nums1:
            j=nums2.index(x)
            if j<len(nums2)-1:
                m=nums2[j]
                c=0
                for x in nums2[j+1:]:
                    if x>m:
                        res.append(x)
                        c=1
                        break
                if c==0:
                    res.append(-1)
            else:
                res.append(-1)
        return res

        
