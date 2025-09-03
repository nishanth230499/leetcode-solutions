# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = preorder.pop(0)
        p1 = []
        i1 = []
        cur = inorder.pop(0)
        while cur != root:
            i1.append(cur)
            p1.append(preorder.pop(0))
            cur = inorder.pop(0)
        return TreeNode(root, self.buildTree(p1, i1), self.buildTree(preorder, inorder))