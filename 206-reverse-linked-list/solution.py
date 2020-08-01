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
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head:
#             return head

#         curr = head
#         while curr.next:
#             temp = curr.next
#             curr.next = curr.next.next
#             temp.next = head
#             head = temp
#         return head
