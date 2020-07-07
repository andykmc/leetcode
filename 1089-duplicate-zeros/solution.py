'''
Time: O(n)
Space: O(1)

'''


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length_ = len(arr) - 1
        dup = 0

        for left in range(len(arr)):
            if left > length_ - dup:
                break
            if arr[left] == 0:
                if left == length_ - dup:
                    arr[len(arr) - 1] = arr[left]
                    length_ -= 1
                    break
                dup += 1
        last = length_ - dup

        for i in range(last, -1, -1):
            arr[i + dup] = arr[i]
            if arr[i] == 0:
                dup -= 1
                arr[i + dup] = arr[i]


# Slow solution:
'''
Time: O(n^2)
Space: O(1)
'''


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        def insert(ele, pos, arr):
            for i in range(pos + 1, len(arr))[::-1]:
                arr[i] = arr[i - 1]
            if pos < len(arr):
                arr[pos] = ele

        i = 0
        while i < len(arr):
            if arr[i] == 0:
                insert(0, i + 1, arr)
                i += 2
            else:
                i += 1
