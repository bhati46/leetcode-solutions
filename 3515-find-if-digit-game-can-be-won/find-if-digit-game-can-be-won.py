class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s=0
        x=0
        for i in nums:
            if i>=10:
                s+=i
            elif i<10:
                x+=i
        return x!=s