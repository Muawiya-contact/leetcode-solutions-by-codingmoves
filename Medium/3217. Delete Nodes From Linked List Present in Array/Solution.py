# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        to_delete = set(nums)   # store nums in a set for fast lookup
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head

        while curr:
            if curr.val in to_delete:
                prev.next = curr.next   # skip current node
            else:
                prev = curr
            curr = curr.next

        return dummy.next
