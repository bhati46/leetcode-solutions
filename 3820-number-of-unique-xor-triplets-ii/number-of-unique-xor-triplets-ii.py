class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        x = max(nums) << 1
        y = [False] * x
        for i in nums:
            for j in nums:
                y[i ^ j] = True
        z = [0] * x
        for i in range(x):
            if y[i]:
                for j in nums:
                    z[i ^ j] = 1
        return sum(z)