class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s=s.split()
        y=""
        for i in range(k):
            y+=s[i]
            y+=" "
        return y.rstrip()