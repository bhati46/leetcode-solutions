class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        x=[0]*n
        y=[1]*n
        z=[1]*n
        for i in range(1,n):
            y[i]=nums[i-1]*y[i-1]
        for j in range(n-2,-1,-1):
            z[j]=nums[j+1]*z[j+1]
        for k in range(n):
            x[k]=y[k]*z[k]
        return x