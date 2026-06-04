class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        x=nums[::-1]
        nums.extend(x)
        return nums