class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        x=min(nums)
        y=max(nums)
        z=[]
        for i in range(x,y):
            if i not in nums:
                z.append(i)
        return z