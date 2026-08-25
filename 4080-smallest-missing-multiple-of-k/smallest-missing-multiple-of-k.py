class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        x=set(nums)
        i=1
        while True:
            if k*i not in x:
                return k*i
            i+=1