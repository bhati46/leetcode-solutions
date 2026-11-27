# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        a=[]
        b=[]
        def fun(b,cur,cursum):
            nonlocal a
            if cur == None:
                return 
            cursum+=cur.val
            b.append(cur.val)
            if cur.left == None and cur.right == None:
                if cursum == targetSum:
                    a.append(b.copy())
            if cur.left!=None:
                fun(b,cur.left,cursum)
            if cur.right!=None:
                fun(b,cur.right,cursum)
            b.pop()
        fun(b,root,0)
        return a