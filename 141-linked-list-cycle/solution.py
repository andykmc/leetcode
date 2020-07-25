'''
Space: O(1)
Time: O(n)
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = None if head is None else head.next
        while fast is not None:
            slow = slow.next
            fast = fast.next.next if fast.next is not None else None
            if slow == fast:
                return True
        return False
