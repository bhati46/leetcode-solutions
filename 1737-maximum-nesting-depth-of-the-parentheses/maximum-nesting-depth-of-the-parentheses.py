class Solution:
    def maxDepth(self, s: str) -> int:
        c=0
        ma=0
        for i in range(len(s)):
            if s[i]=="(":
                c+=1
                ma=max(ma,c)
            elif s[i]==")":
                c-=1
        return ma