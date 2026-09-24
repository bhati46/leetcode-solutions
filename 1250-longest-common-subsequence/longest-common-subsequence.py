class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1] * len(text2) for _ in range(len(text1))]
        def fun(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            take = 0
            if text1[i] == text2[j]:
                take = 1 + fun(i + 1, j + 1)
            else:
                take = max(fun(i + 1, j), fun(i, j + 1))
            dp[i][j] = take
            return dp[i][j]
        return fun(0,0)
