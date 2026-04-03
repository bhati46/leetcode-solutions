class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            elif nums[i]%2!=0:
                nums[i]=1
        z = nums.count(0)
        o = len(nums) - z

        return [0]*z+[1]*o
