class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        ans=[]
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        for i,j in envelopes:
            if  len(ans)==0 or j>ans[-1]:
                ans.append(j)
            else:
                l=0
                h=len(ans)-1
                while l <= h :
                    mid=l+(h-l)//2
                    if ans[mid] >= j:
                        h=mid-1
                    else:
                        l=mid+1
                ans[l]=j
        return len(ans)