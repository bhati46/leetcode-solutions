class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        r=[]
        z=max(candies)
        for i in candies:
            if i+extraCandies>=z:
                r.append(True)
            else:
                r.append(False)
        return r