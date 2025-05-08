from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        while head and head.val == val:
            head = head.next
        if head == None:
            return head
        first = head

        while head:
            while head.next and head.next.val == val:
                head.next = head.next.next
            head = head.next

        return first


class Runner:

    def create_linked_list_from_array(arr: list) -> ListNode | None:
        """
        Constructs a linked list from an array.
        Args:
            arr: A list of values to be converted into a linked list.
        Returns:
            The head of the constructed linked list, or None if the array is empty.
        """
        if not arr:
            return None
        
        head = ListNode(arr[0])
        current = head
        for i in range(1, len(arr)):
            current.next = ListNode(arr[i])
            current = current.next
        return head


    # Example of how to use it (optional, for demonstration):
if __name__ == '__main__':
    my_array = [1, 2, 6, 3, 4, 5, 6]
    linked_list_head = Runner.create_linked_list_from_array(my_array)

    # Helper to print the linked list
    def print_linked_list(node):
        while node:
            print(node.val, end=" -> " if node.next else "")
            node = node.next
        print() # for newline

    print_linked_list(linked_list_head) # Output: 1 -> 2 -> 3 -> 4 -> 5

    sol = Solution()
    head = sol.removeElements(linked_list_head, 6)
    print_linked_list(head)
