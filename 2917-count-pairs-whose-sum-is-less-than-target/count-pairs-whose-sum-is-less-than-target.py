class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        c=0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] +nums[j]<target:
                    c+=1
        return c