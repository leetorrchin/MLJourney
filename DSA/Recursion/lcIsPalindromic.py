# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        ## We need some method of storing a tracker for the front of the list to compare with 
        ## the end when we recurse.
        self.front = head

        def symmetric(node):
            # if list is empty, obviously return True
            if (node is None):
                return True
            
            ## We want to return false, if the palindromic-ness returns false at any point even
            ## if its just one pair, so having this preceed everything else, we gurantee we skip
            ## the rest of the code in winding down from stack calls, and return false
            
            if not symmetric(node.next):
                return False

            # Now we want to compare the pair of nodes, which is quite simple, we return false
            if (node.val != self.front.val):
                return False

            # If it passed the previous case, it means it was obviously true, and hence we return true,
            # and we move on the check the next pair. This obviously mean we also need to update our 
            # front tracker.
            self.front = self.front.next
            return True

        return symmetric(head)

            





        