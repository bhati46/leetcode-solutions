class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        x=[]
        for i in range(1,len(height)):
            if height[i-1]>threshold:
                x.append(i)
        return x