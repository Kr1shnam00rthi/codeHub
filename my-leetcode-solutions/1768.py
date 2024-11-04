class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        res=""
        for k in range(min(len(word1),len(word2))):
            res+=word1[k]
            res+=word2[k]
            i+=1
            j+=1
        while i<len(word1):
            res+=word1[i]
            i+=1
        while j<len(word2):
            res+=word2[j]
            j+=1
        return res
