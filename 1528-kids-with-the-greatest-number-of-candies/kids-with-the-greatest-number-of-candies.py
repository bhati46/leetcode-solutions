class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        r=[]
        for i in candies:
            z=max(candies)
            if i+extraCandies>=z:
                r.append(True)
            else:
                r.append(False)
        return r