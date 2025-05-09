class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        first = head
        while (head.next):
            if (head.next.val != head.val):
                head = head.next
            else:
                pointer = head.next
                while (pointer.next):
                    if (pointer.next.val != head.val):
                        head.next = pointer.next
                        break

                head = head.next
        # head.next = None
        return first

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

lst = [1, 1, 2, 3, 3]
# lst = [1, 1, 2]

head = None
for val in reversed(lst):
    head = ListNode(val, head)


sol = Solution()
print(sol.deleteDuplicates(head))





"""
    def deleteDuplicates(self, head):
        
        while (head.next):
            if (head.next.val != head.val):
                head = head.next
            else:
                pointer = head.next
                while (pointer.next):
                    if (pointer.next.val != head.val):
                        head.next = pointer
                        head = head.next
                head.next = None
"""