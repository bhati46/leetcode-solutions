from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        x=Counter(nums)
        y=[]
        for i in x:
            if x[i]==2:
                y.append(i)
        return y