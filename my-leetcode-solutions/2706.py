class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        count=0
        m=money
        while count<2:
            i=prices.index(min(prices))
            money-=prices.pop(i)
            count+=1
        if money<0:
            return m
        return money
