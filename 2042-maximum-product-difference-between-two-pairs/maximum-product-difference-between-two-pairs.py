class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        x=nums[-1]*nums[-2]
        y=nums[0]*nums[1]
        return x-y