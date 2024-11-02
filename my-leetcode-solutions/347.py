class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements=dict()
        num=set(nums)
        for x in num:
            elements.update({x:nums.count(x)})
        element=[]
        res=[]
        for x in elements:
            element.append([x,elements[x]])
        for i in range(len(element)):
            for j in range(len(element)-1-i):
                if element[j][1]<element[j+1][1]:
                    element[j],element[j+1]=element[j+1],element[j]
        for i in range(k):
            res.append(element[i][0])
        return res
