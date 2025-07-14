# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        result = 0
        while head:
            result = result * 2 + head.val
            head = head.next
        return result

# Helper function to create linked list from Python list
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Example usage
head = create_linked_list([1, 0, 1, 1])
sol = Solution()
print(sol.getDecimalValue(head))  # Output: 11
