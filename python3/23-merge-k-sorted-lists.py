# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode()
        current = head
        while True:
            min_indeces = None
            for i in range(len(lists)):
                if lists[i] != None:
                    if min_indeces == None or lists[i].val < lists[min_indeces[0]].val:
                        min_indeces = [i]
                    elif lists[i].val == lists[min_indeces[0]].val:
                        min_indeces.append(i)
            
            if min_indeces == None:
                return head.next
            
            for min_index in min_indeces:
                current.next = lists[min_index]
                current = current.next
                while current.next and current.next.val == current.val:
                    current = current.next
                lists[min_index] = current.next
