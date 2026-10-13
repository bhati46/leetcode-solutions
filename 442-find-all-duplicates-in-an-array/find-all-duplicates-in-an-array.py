class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        x=Counter(nums)
        y=[]
        for i in x:
            if x[i]==2:
                y.append(i)
        return y