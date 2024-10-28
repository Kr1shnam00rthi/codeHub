class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a=="0" and b=="0":
            return "0"
        def bintoint(n):
            res=0
            n=n[::-1]
            for i in range(len(n)):
                res=res+(2**i)*int(n[i])
            return res

        def intobin(n):
            res=""
            while n!=0:
                if n%2==0:
                    res+="0"
                else:
                    res+="1"
                n=n//2
            return res[::-1]
        return intobin(bintoint(a)+bintoint(b))
