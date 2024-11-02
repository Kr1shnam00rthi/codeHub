class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        for i in range(k):
            t=nums.pop(len(nums)-1)
            nums.insert(0,t)
        return nums

