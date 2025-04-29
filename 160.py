# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        A = set()
        nodeA = headA
        while nodeA:
            A.add(nodeA)
            nodeA = nodeA.next
        
        nodeB = headB
        while nodeB:
            if nodeB in A:
                return nodeB
            nodeB = nodeB.next
        
        return None

        