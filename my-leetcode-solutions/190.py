class Solution:
    def reverseBits(self, n: int) -> int:
        n=str(bin(n))
        n=n[2:]
        while len(n)<32:
            n="0"+n
        res=0
        for i in range(0,len(n)):
            res+=(int(n[i])*(2**i))
        return res
