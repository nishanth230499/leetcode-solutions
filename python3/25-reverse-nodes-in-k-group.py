# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        head = ListNode(next=head)
        cur_left = head
        
        while True:
            cur_right = cur_left
            i = 0
            while True:
                if cur_right.next:
                    cur_right = cur_right.next
                    i += 1
                    if i == k:
                        break
                else:
                    break
            if i != k:
                break
            cur_right = cur_left.next
            cur = None
            for i in range(k):
                temp = cur_left.next.next
                # print(temp)
                cur_left.next.next = cur
                cur = cur_left.next
                cur_left.next = temp
            cur_left.next = cur
            cur_right.next = temp
            cur_left = cur_right
        return head.next





        