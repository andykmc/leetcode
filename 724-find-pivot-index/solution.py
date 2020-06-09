class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        for i, num in enumerate(nums):
            if left == right - left - num:
                return i
            left += num
        return -1
