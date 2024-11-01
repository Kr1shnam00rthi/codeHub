class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        num=(num**0.5)
        diff = num-int(num)
        return diff==0.0
