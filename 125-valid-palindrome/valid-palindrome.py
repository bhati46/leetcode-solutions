class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=""
        for i in range(len(s)):
            if s[i].isalnum():
                x+=s[i].lower()
        return x==x[::-1]