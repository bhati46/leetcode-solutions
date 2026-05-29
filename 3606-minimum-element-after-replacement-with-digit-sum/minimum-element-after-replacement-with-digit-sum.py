class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            y=0
            x=str(nums[i])
            for j in x:
                y+=int(j)
            nums[i]=y
        return min(nums)
