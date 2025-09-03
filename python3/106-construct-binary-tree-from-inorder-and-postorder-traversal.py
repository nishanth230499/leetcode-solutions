# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        i_map = {val: i for i, val in enumerate(inorder)}

        postorder_index = len(postorder) - 1
        
        def rec(s, e):
            if s > e:
                return None
            nonlocal postorder_index
            root = postorder[postorder_index]
            postorder_index -= 1
            inorder_index = i_map[root]
            right_tree = rec(inorder_index + 1, e)
            left_tree = rec(s, inorder_index - 1)
            return TreeNode(root, left_tree, right_tree)
        return rec(0, len(inorder) - 1)