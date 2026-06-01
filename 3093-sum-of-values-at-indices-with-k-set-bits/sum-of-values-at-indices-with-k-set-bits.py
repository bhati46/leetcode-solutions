class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        x=[]
        y=0
        for i in range(len(nums)):
            x.append(bin(i)[2:])
        for i in range(len(x)):
            if x[i].count("1")==k:
                y+=nums[i]
        return y