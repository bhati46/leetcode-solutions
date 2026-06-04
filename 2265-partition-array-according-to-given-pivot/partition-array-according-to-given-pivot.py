class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        x=[]
        y=[]
        z=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                x.append(nums[i])
            elif nums[i]==pivot:
                z.append(pivot)
            else:
                y.append(nums[i])
        x.extend(z) 
        x.extend(y)
        return x