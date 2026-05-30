class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a,b,c=nums[0],nums[1],nums[2]
        m=max(a,b,c)
        if a+b+c-m <= m:
            return "none"
        if a == b == c:
            return "equilateral"
        if a == b or b == c or a == c:
            return "isosceles"
        return "scalene"