class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        for x in nums:
            if x%2==0:
                even.append(x)
            else:
                odd.append(x)
        even.extend(odd)
        return even
