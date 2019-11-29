# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        lessThan = ListNode(0)
        greaterThan = ListNode(0)
        lessThanTail = lessThan
        greaterThanTail = greaterThan
        
        
        while head is not None:
            
            if head.val < x:
                lessThanTail.next = head
                lessThanTail = lessThanTail.next
            else:
                greaterThanTail.next = head
                greaterThanTail = greaterThanTail.next
            
            head = head.next
            
        
        greaterThanTail.next = None
        lessThanTail.next = greaterThan.next
        return lessThan.next
        
