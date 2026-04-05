class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        r=[1]*len(nums)
        for i in range(len(nums)):
            r[i]=nums[nums[i]]
        return r
