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
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        slow = head
        fast = head.next
        while slow is not fast and fast is not None:
            slow = slow.next
            fast = None if fast.next is None else fast.next.next
        if fast is None:
            return None

        slow = slow.next  # This step is need since fast is started at head.next
        slow2 = head
        while slow2 is not slow:
            slow2 = slow2.next
            slow = slow.next
        return slow2
