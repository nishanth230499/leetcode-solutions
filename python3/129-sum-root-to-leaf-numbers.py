# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def rec(cur, pre_num):
            if cur.left == None and cur.right == None:
                self.res += pre_num * 10 + cur.val
                return
            
            if cur.left:
                rec(cur.left, pre_num * 10 + cur.val)
            
            if cur.right:
                rec(cur.right, pre_num * 10 + cur.val)
        
        rec(root, 0)
        return self.res