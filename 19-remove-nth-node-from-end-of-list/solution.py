'''
Space: O(1)
Time: O(n)
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        while n > 0:
            fast = fast.next
            n -= 1
        if fast is None:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return head

#         count = 1
#         fast = head
#         slow = head
#         while fast is not None:
#             fast = fast.next
#             if count < n + 2:
#                 count += 1
#             else:
#                 slow = slow.next
#         if count == n + 2:
#             slow.next = slow.next.next if slow.next is not None else None
#         else:
#             head = head.next

#         return head
