class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i=0
        while True:
            t=2**i
            if t==n:
                return True
            elif t>n:
                return False
            i+=1
        return False
