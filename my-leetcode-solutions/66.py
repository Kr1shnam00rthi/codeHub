class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums=""
        for x in digits:
            nums+=str(x)
        nums=int(nums)+1
        n=[]
        while nums>0:
            n.append(nums%10)
            nums=nums//10
        return n[::-1]
        
