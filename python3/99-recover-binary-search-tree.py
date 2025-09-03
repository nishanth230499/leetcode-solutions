# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        def rec(r):
            if r == None:
                return
            rec(r.left)
            nodes.append(r)
            rec(r.right)
        rec(root)

        n1 = None
        n2 = None
        for i in range(len(nodes) - 1):
            if nodes[i].val > nodes[i+1].val:
                if n1 == None:
                    n1 = nodes[i]
                    n2 = nodes[i+1]
                else:
                    n2 = nodes[i+1]
        n1.val, n2.val = n2.val, n1.val
    