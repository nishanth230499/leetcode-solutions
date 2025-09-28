# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1

        def rec(cur, cur_sum):
            if not cur:
                return 0
            prefix[cur_sum + cur.val] += 1
            res1 = rec(cur.left, cur_sum + cur.val)
            res2 = rec(cur.right, cur_sum + cur.val)
            prefix[cur_sum + cur.val] -= 1


            return prefix[cur_sum + cur.val - targetSum] + res1 + res2
        
        return rec(root, 0)

