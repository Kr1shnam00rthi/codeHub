class Solution:
    def frequencySort(self, s: str) -> str:
        ele={}
        for i in range(len(s)):
            if s[i] not in ele:
                ele[s[i]]=1
            else:
                t=ele[s[i]]
                ele[s[i]]=t+1
        res=""
        mydict=[[key,value] for key,value in ele.items()]
        for i in range(len(mydict)):
            for j in range(0,len(mydict)-i-1):
                if mydict[j][1]<mydict[j+1][1]:
                    mydict[j],mydict[j+1]=mydict[j+1],mydict[j]
        for x in mydict:
            for i in range(x[1]):
                res+=x[0]
        return res
