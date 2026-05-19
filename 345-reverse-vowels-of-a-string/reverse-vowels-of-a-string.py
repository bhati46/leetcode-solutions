class Solution:
    def reverseVowels(self, s: str) -> str:
        x=[]
        for i in range(len(s)):
            if s[i].lower() in ["a","e","i","o","u"]:
                x.append(s[i])
        x=x[::-1]
        s=list(s)
        j=0
        for i in range(len(s)):
            if s[i].lower() in ["a","e","i","o","u"]:
                s[i]=x[j]
                j+=1
        return "".join(s)