class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        x="qwertyuiopasdfghjklmnbvcxz"
        s=set(sentence)
        n=set(x) 
        if len(s)==len(n): 
            return True 
        else: 
            return False
