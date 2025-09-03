# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def rec(cur, pre_res):
            if cur.left == None and cur.right == None:
                res.append(pre_res + [str(cur.val)])
            
            if cur.left:
                rec(cur.left, pre_res + [str(cur.val)])
            
            if cur.right:
                rec(cur.right, pre_res + [str(cur.val)])
        
        rec(root, [])

        return list(map(lambda a: "->".join(a), res))
