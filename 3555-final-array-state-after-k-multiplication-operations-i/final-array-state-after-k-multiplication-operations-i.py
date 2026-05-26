class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while(k>0):
            for i in range(len(nums)):
                x=min(nums)
                if nums[i]==x:
                    nums[i]=nums[i]*multiplier
                    break
            k-=1
        return nums