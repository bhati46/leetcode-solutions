class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        x=set(arr)
        if arr.count(0) >= 2:
            return True
        for i in x:
            if i!=0 and 2*i in x:
                return True
        return False