# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        currNode = res
        while (list1 != None and list2 != None):
            nextNode = None
            if list1.val > list2.val:
                nextNode = ListNode(list2.val)
                list2 = list2.next
            else:
                nextNode = ListNode(list1.val)
                list1 = list1.next
            currNode.next = nextNode
            currNode = nextNode
        if list1:
            currNode.next = list1
        elif list2:
            currNode.next = list2
        return res.next

        