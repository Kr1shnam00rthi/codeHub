class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        e=len(numbers)-1
        while l<e:
            if numbers[l]+numbers[e]==target:
                return [l+1,e+1]
            elif numbers[l]+numbers[e]>target:
                e-=1
            elif numbers[l]+numbers[e]<target:
                l+=1
