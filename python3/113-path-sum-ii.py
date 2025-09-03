# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root == None:
            return []
        
        if root.left == None and root.right == None:
            return [[root.val]] if root.val == targetSum else []
        
        return list(map(lambda a: [root.val] + a,(self.pathSum(root.left, targetSum - root.val) + self.pathSum(root.right, targetSum - root.val))))