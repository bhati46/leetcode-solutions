class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        x=set(word)
        c=0
        for i in x:
            if i.islower() and i.upper() in x and word.rindex(i) < word.index(i.upper()):
                c+=1
        return c