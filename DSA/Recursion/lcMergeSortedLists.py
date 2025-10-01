# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # If we reach the end of one list, we simply return the other because it is already sorted.
        if (list1 is None):
            return list2
        if (list2 is None):
            return list1

        # So lets first consider the case where the first list is less than the second list, in this   
        # case, we would want to add the first list's node to the list first. 
        if (list1.val < list2.val):
            #to attach the node the the rest of the list
            list1.next = self.mergeTwoLists(list1.next, list2) 
            # we return this node first
            return list1
        else:
            #otherwise this, because we prioritise list2 over list1, when they are of equal value.
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
            
        