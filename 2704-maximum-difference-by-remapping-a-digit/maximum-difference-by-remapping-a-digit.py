class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        maxi = s
        for digit in s:
            if digit != "9":
                maxi = s.replace(digit, "9")
                break
        mini = s.replace(s[0], "0")

        return int(maxi) - int(mini)