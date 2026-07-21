class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        x = set(nums)
        for i in nums:
            y = int(str(i)[::-1])
            x.add(y)
        return len(x)