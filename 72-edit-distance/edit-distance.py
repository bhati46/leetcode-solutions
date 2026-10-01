class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[-1]*(len(word2)+1) for _ in range(len(word1)+1)]
        def fun(i,j):
            if i==len(word1):
                return (len(word2)-j)
            if j==len(word2):
                return (len(word1)-i)
            if dp[i][j]!=-1:
                return dp[i][j]
            # this checks if char1 is equal to char2
            if word1[i]==word2[j]:
                dp[i][j]=fun(i+1,j+1)
            # in this we are moving the pointers 
            else:
                # we are taking min of insert, replace and delete
                dp[i][j]=1+min(fun(i+1,j+1) # replace(we are replacing that char which are not  equal )
                ,fun(i,j+1), # insert( we  are inserting the char which is not equal not the other char )
                fun(i+1,j)  # delete (we are  deleting the char if that is not equal )
                ) 
            return dp[i][j]
        return fun(0,0)