# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode()
        current_node = l3
        carry = 0
        while l1 != None or l2 != None or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            sum = a + b + carry

            new_node = ListNode(sum % 10)
            carry = sum // 10

            current_node.next = new_node
            current_node = new_node

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

        return l3.next


        