class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        res=[]
        a=None
        if x<0:
            x=-x
            while x>0:
                res.append(str(x%10))
                x=x//10
            a=-1*int("".join(res))
        else:
            while x>0:
                res.append(str(x%10))
                x=x//10
            a=int("".join(res))
        if a> -2 **31 and a<2**31 -1:
            return a
        return 0
