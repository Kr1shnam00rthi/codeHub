class Solution:
    # two pointers
    def maxArea(self, height: List[int]) -> int:
        res=0
        l=0
        e=len(height)-1
        while l<e:
            amt_water=min(height[e],height[l])*(e-l)
            if res<amt_water:
                res=amt_water
            if height[l]<height[e]:
                l+=1
            else:
                e-=1
        return res
