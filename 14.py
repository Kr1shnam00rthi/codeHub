class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str1=min(strs)
        res=""
        l=len(strs)
        for i in range(len(str1)):
            count=0
            for j in range(l):
                if i<len(strs[j]) and str1[i]==strs[j][i]:
                    count+=1
            if count==l:
                res+=str1[i]
            else:
                break
        return res
