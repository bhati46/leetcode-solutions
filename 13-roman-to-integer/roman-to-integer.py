class Solution:
    def romanToInt(self, s: str) -> int:
        x = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1 and x[s[i]] < x[s[i + 1]]:
                ans -= x[s[i]]
            else:
                ans += x[s[i]]
        return ans