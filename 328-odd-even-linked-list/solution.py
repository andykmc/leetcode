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
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        head2 = head.next
        odd = head
        even = head.next
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

        odd.next = head2
        return head

# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         if not head:
#             return head

#         head2 = head.next
#         odd = head
#         even = head.next
#         while even:
#             if odd.next:
#                 odd.next = odd.next.next if odd.next.next else None
#                 odd = odd.next if odd.next else odd
#             if even.next:
#                 even.next = even.next.next
#             even = even.next

#         odd.next = head2
#         return head

# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         if not head:
#             return head

#         head2 = head.next
#         odd = head
#         even = head.next
#         while 1:
#             if odd.next:
#                 odd.next = odd.next.next if odd.next.next else head2
#                 odd = odd.next
#             else:
#                 odd.next = head2
#                 return head
#             if even.next:
#                 even.next = even.next.next
#                 even = even.next
#             else:
#                 return head
