class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k%=len(nums)
        x=[]
        for i in range(len(nums)-k,len(nums)):
            x.append(nums[i])
        for i in range(k):
            nums.pop()
        nums[:]=x+nums
        """
        Do not return anything, modify nums in-place instead.
        """
        