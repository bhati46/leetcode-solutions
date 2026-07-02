class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            x = 26 - (ord(s[i]) - ord('a'))
            ans += x * (i + 1)
        return ans