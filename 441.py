class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows=0
        i=1
        while n!=0:
            if n-i >=0:
                rows+=1
                n-=i
                i+=1
            else:
                break
        return rows
