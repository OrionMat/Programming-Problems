# Merge Two Sorted Linke Lists

# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.
# e.g:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list:
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def printList(self):
        while(self):
            print(self.val)
            self = self.next
        print('\n')

# faster than 92.27% less memory used than 5.75%
class Solution(object):
    def mergeTwoLists(self, L1, L2):
        """
        :type L1: ListNode
        :type L2: ListNode
        :rtype: ListNode
        """
        L1prev, L2prev = ListNode(None), ListNode(None)
        L1prev.next = L1
        root = L1prev
        while L2:
            root.printList()
            if L1:
                if L2.val < L1.val: 
                    # prepend L2 node to L1
                    L2prev = L2
                    L2 = L2.next
                    L2prev.next = L1
                    L1prev.next = L2prev
                    L1prev = L2prev
                else:
                    # move to next L1 node
                    L1prev = L1
                    L1 = L1.next
            else:
                L1prev.next = L2
                break
        return root.next