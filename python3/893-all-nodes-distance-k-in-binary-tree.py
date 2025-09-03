# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.res = []
        def add_res(r, l):
            if r == None:
                return
            if l == 0:
                self.res.append(r.val)
                return
            add_res(r.left, l-1)
            add_res(r.right, l-1)

        def search(r):
            if r == None:
                return None
            if r.val == target.val:
                add_res(r, k)
                return 1
            l_len = search(r.left)
            r_len = search(r.right)
            if l_len == k or r_len == k:
                add_res(r, 0)
                return None
            if l_len and l_len < k:
                    add_res(r.right, k - l_len - 1)
                    return l_len + 1
            if r_len and r_len < k:
                    add_res(r.left, k - r_len - 1)
                    return r_len + 1
        
        search(root)
        return self.res
