class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d=dict(knowledge)
        y=""
        i=0
        while i<len(s):
            if s[i]=="(": # checking if the string has ( in s 
                key=""
                j=i+1
                while s[j] !=")":# it will work till the  ) has ended 
                    key+=s[j]
                    j+=1
                if key in d: 
                    y+=d[key] # this will add the value of key if is in the dict
                else:
                    y+="?" # if key is not in dict so we add ?
                i=j # this is done because it should start iteration where j is ending so it does not go back 
            else:
                y+=s[i] # for other char in th str that are not in bracket 
            i+=1
        return y