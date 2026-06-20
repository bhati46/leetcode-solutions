class Solution:
    def passwordStrength(self, password: str) -> int:
        x=0
        password=set(password)
        for i in password:
            if i.islower():
                x+=1
            elif i.isupper():
                x+=2
            elif i.isdigit():
                x+=3
            else:
                x+=5
        return x