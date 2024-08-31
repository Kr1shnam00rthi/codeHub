class Solution:
    def search(self,num,target):
        l=0
        e=len(num)-1
        while l<=e:
            m=(l+e)//2
            if num[m]==target:
                return 1
            elif num[m]>target:
                e=m-1
            elif num[m]<target:
                l=m+1
        return 0
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num=[]
        for i in range(len(matrix)):
            if target<=matrix[i][-1]:
                return self.search(matrix[i],target)
        
