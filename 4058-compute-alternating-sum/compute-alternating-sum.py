class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        x=0
        y=0
        for i in range(len(nums)):
            if i%2!=0:
                y+=nums[i]
            else:
                x+=nums[i]
        return x-y