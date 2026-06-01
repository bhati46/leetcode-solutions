class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s=[]
        j=0
        for i in range(1,n+1):
            s.append("Push")
            if i == target[j]:
                j += 1
                if j == len(target):
                    break
            else:
                s.append("Pop")
        return s