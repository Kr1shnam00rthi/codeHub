class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count=-1
        for x in s:
            if x=='1':
                count+=1
        res="1"
        l=len(s)-1-count
        for _ in range(l):
            res+="0"
        for _ in range(count):
            res+="1"
        return res[::-1]
