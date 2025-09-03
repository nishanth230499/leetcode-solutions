"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        head_copy = None
        current = head
        prev_copy = head_copy
        copy_map = {None : None}
        while current:
            next_copy = Node(current.val)
            copy_map[current] = next_copy
            if prev_copy:
                prev_copy.next = next_copy
                prev_copy = next_copy
            else:
                head_copy = next_copy
                prev_copy = next_copy
            current = current.next
        
        current = head
        current_copy = head_copy

        while current:
            copy_map[current].random = copy_map[current.random]
            current = current.next
        
        return head_copy
