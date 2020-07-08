'''
Space: O(1)
Time: O(m + n)
'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos = len(nums1) - 1
        left = m - 1
        right = n - 1
        while left >= 0 or right >= 0:
            if left >= 0 and right >= 0 and nums1[left] > nums2[right] or right < 0:
                nums1[pos] = nums1[left]
                left -= 1
            else:
                nums1[pos] = nums2[right]
                right -= 1
            pos -= 1
