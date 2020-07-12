'''
Space: O(1)
Time: O(n)
'''


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        i = 0
        n = len(A)

        while i < n - 1 and A[i] < A[i + 1]:
            i += 1

        if i == 0 or i == n - 1:
            return False

        while i < n - 1 and A[i] > A[i + 1]:
            i += 1

        return i == n - 1
