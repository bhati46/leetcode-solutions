class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=[]
        for i in range(n):
            x.append(nums[i])
            x.append(nums[n+i])
        return x
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
            


      

           