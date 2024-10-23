class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split(" ")
        i=0
        while True:
            if len(s[-i-1])!=0:
                return len(s[-i-1])
            else:
                i+=1
