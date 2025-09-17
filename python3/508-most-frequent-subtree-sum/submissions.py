from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)
        self.highest_count = 0
        def rec(cur):
            if not cur:
                return 0
            sum = cur.val
            sum += rec(cur.left)
            sum += rec(cur.right)

            count[sum] += 1
            self.highest_count = max(self.highest_count, count[sum])

            return sum
        
        rec(root)

        res = []
        for sum in count:
            if count[sum] == self.highest_count:
                res.append(sum)
        
        return res
