class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        x=set(word)
        c=0
        for i in x:
            if i.islower()  and i.upper() in x:
                c+=1
        return c
