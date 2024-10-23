class Solution:
    def firstUniqChar(self, s: str) -> int:
        t=set()
        for i in range(len(s)):
            if s[i] not in t and s.count(s[i])==1:
                return i
            else:
                t.add(s[i])
        return -1
