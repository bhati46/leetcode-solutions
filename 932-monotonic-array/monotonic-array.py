class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        c=0
        x=0
        n=len(nums)-1
        for i in range(n):
            if nums[i] <= nums[i+1]:
                c+=1
            if nums[i] >= nums[i+1]:
                x+=1
        return c == n or x == n