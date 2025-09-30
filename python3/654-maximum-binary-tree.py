# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []

        for num in nums:
            if stack and num > stack[-1].val:
                cur = stack.pop()
                while stack and stack[-1].val < num:
                    stack[-1].right = cur
                    cur = stack.pop()
                stack.append(TreeNode(num, cur))
            else:
                stack.append(TreeNode(num))
                
        cur = stack.pop()
        while stack:
            stack[-1].right = cur
            cur = stack.pop()
        
        return cur
