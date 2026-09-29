class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[-1] * m for _ in range(n)]
        def fun(i, j):
            if j == m:
                return 1
            if i == n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == t[j]:
                dp[i][j] = fun(i + 1, j + 1) + fun(i + 1, j)
            else:
                dp[i][j] = fun(i + 1, j)
            return dp[i][j]
        return fun(0, 0)