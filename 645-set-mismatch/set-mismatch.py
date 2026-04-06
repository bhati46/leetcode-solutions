class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        x=set()
        d=int()
        for i in nums:
            if i in x:
                d=i
            x.add(i)
        n=len(nums)
        x=n*(n+1)//2
        y=sum(nums)
        p=x-(y-d)
        return [d,p]