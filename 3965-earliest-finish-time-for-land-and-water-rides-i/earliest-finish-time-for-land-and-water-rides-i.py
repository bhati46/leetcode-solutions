class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        y = float('inf')  
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                x=landStartTime[i]+landDuration[i] 
                z=max(x,waterStartTime[j])+ waterDuration[j]   
                y=min(y,z)   
                x=waterStartTime[j]+waterDuration[j]   
                z=max(x,landStartTime[i])+landDuration[i]   
                y=min(y,z)   
        return y