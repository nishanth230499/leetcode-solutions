class Node:
    def __init__(self, start_index, end_index, total = 0, left = None, right = None):
        self.start_index = start_index
        self.end_index = end_index
        self.total = total
        self.left = left
        self.right = right

class NumArray:
    def __init__(self, nums: List[int]):
        def create_tree(i, j):
            root = Node(i, j)

            if i == j:
                root.total = nums[i]
                return root
            
            mid = (i + j) // 2

            root.left = create_tree(i, mid)
            root.right = create_tree(mid + 1, j)
            root.total = root.left.total + root.right.total
            return root

        self.range_tree = create_tree(0, len(nums) - 1)

    def update(self, index: int, val: int, root = None) -> None:
        if root == None:
            root = self.range_tree
        if root.start_index == index == root.end_index:
            root.total = val
            return
        if root.start_index <= index <= root.end_index:
            self.update(index, val, root.left)
            self.update(index, val, root.right)
            root.total = root.left.total + root.right.total
        
    def sumRange(self, left: int, right: int, root = None) -> int:
        if root == None:
            root = self.range_tree
        if left <= root.start_index and root.end_index <= right:
            return root.total
        if right < root.start_index or root.end_index < left:
            return 0
        return self.sumRange(left, right, root.left) + self.sumRange(left, right, root.right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)