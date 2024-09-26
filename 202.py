class Solution:
    def cal(self,n):
        s=0
        ele=[]
        while n>0:
            ele.append(n%10)
            n=n//10
        for x in ele:
            s+=pow(x,2)
        return s
    def isHappy(self, n: int) -> bool:
        count=0
        while n!=1:
            if count==10:
                return False
            n=self.cal(n)
            print(n)
            if n==1:
                return True
            count+=1
        return True
            
