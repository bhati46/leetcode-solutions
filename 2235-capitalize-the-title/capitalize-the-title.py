class Solution:
    def capitalizeTitle(self, title: str) -> str:
        x=title.split()
        sum=""
        for i in x:
            if len(i)>=3:
                n=i.capitalize()
                sum+=n+" "
            else:
                y=i.lower()
                sum+=y+" "
        return sum.rstrip()