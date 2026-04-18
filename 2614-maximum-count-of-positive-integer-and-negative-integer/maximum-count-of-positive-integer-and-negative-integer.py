class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        x=0
        y=0 
        for i in range(len(nums)): 
            if nums[i]>0: 
                x+=1 
            elif nums[i]<0: 
                y+=1 
        return max(x,y)