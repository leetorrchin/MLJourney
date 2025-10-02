# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        if (head is None):
            return None
        head.next = self.removeElements(head.next, val)
        if (head.val == val):
            return head.next
        else:
            return head




        