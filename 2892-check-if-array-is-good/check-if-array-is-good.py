class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        x=nums[-1]
        if len(nums) != x + 1:
            return False
        if nums[-1] != nums[-2]:
            return False
        for i in range(x-1):
            if nums[i] != i + 1:
                return False
        return True