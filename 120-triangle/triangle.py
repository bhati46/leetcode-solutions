class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ma = float("inf")
        dp = [[ma] * len(triangle) for i in range(len(triangle))]
        def fun(dp):
            for i in range(len(triangle)):
                for j in range(len(triangle[i])):
                    if i == 0 and j == 0:
                        dp[i][j] = triangle[i][j]
                        continue
                    if i - 1 < 0:
                        up = ma
                    else:
                        up = dp[i - 1][j]
                    if j - 1 < 0 or i - 1 < 0:
                        upleft = ma
                    else:
                        upleft = dp[i - 1][j - 1]
                    dp[i][j] = min(up, upleft) + triangle[i][j]
            return min(dp[-1])
        return fun(dp)