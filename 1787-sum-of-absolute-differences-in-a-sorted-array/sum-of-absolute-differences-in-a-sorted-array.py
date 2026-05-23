class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        x=[0]*len(nums)
        total=sum(nums)
        leftsum=0
        for i in range(len(nums)):
            rightsum = total-leftsum-nums[i]
            left = nums[i]*i - leftsum
            right = rightsum-nums[i]*(len(nums) - i - 1)
            x[i] = left+right
            leftsum += nums[i]
        return x