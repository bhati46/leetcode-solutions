class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        x=[]
        for i in range(len(nums)):
            if i==0:
                x.append(nums[i])
            else:
                x.append(nums[i]+x[i-1])
        return x