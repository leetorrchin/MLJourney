# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if (head is None):
            return None

        if (head.next is None):
            return head

        newhead = self.reverseList(head.next)
        # By doing this, we're essentially flipping the relationship, so we don't need to figure
        # a way to traverse to the end of the LL, and we know for sure its consectuive
        head.next.next = head
        # break the ascending link
        head.next = None
        #return the newhead
        return newhead
        
        