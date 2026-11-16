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
        def fun(b,curroot,currsum):
            nonlocal a
            if curroot == None:
                return 
            currsum+=curroot.val
            b.append(curroot.val)
            if curroot.left == None and curroot.right ==None:
                if currsum == targetSum:
                    a.append(b.copy())
            if curroot.right!=None:
                fun(b,curroot.right,currsum)
            if curroot.left!=None:
                fun(b,curroot.left,currsum)
            b.pop()
        fun(b,root,0)
        return a