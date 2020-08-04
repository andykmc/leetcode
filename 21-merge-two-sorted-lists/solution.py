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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = curr = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2

        return dummy.next

#         left = l1
#         right = l2
#         curr = None
#         if None in (left, right):
#             return left or right

#         if left.val <= right.val:
#             curr = left
#             left = left.next
#         else:
#             curr = right
#             right = right.next

#         while left and right:
#             if left.val <= right.val:
#                 curr.next = left
#                 curr = curr.next
#                 left = left.next
#             else:
#                 curr.next = right
#                 curr = curr.next
#                 right = right.next

#         curr.next = left or right

#         return l1 if l1.val <= l2.val else l2
