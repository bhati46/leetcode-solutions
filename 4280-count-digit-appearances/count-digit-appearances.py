class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        c=0
        digit=str(digit)
        for i in range(len(nums)):
            x=str(nums[i])
            for j in range(len(x)):
                if x[j]==digit:
                    c+=1
        return c