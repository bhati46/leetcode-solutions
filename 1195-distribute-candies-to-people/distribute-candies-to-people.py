class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        i = 0
        give = 1
        while candies > 0:
            if candies >= give:
                ans[i] += give
                candies -= give
            else:
                ans[i] += candies
                candies = 0
            give += 1
            i = (i + 1) % num_people
        return ans