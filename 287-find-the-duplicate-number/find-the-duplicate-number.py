from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x=Counter(nums)
        for i in x:
            if x[i]>=2:
                return i