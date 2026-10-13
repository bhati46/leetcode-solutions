class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        ans=[nums[0]]
        for i in nums:
            if i > ans[-1]:
                ans.append(i)
            else:
                l=0
                h=len(ans)-1
                while l <= h :
                    mid=l+(h-l)//2
                    if ans[mid] >= i:
                        h=mid-1
                    else:
                        l=mid+1

                ans[l]=i

        return len(ans)