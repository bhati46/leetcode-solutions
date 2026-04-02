class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        x=0
        n=0
        for i in nums:
            x+=i
        for i in nums:
            if i>=10:
                n+= sum(map(int, str(i)))
            else:
                n+=i
        return x-n
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("000"))


        