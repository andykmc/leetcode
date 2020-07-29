'''
Space: O(1)
Time: O(m + n)
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        pA = headA
        pB = headB
        while pA is not None and pB is not None:
            if pA is pB:
                return pA
            pA = pA.next
            pB = pB.next
        if pA is None:
            pA = headB
        else:
            pB = headA
        while pA is not None and pB is not None:
            if pA is pB:
                return pA
            pA = pA.next
            pB = pB.next
        if pA is None:
            pA = headB
        else:
            pB = headA
        while pA is not None and pB is not None:
            if pA is pB:
                return pA
            pA = pA.next
            pB = pB.next

        if pA is pB:
            return pA
        else:
            return None
