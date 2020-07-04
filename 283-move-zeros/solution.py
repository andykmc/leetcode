'''
Time: O(n)
Space: O(1)
'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left] = nums[i]
                left += 1
        for i in range(left, len(nums)):
            nums[i] = 0


# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         left = 0
#         right = 0
#         while right < len(nums):
#             if nums[right] != 0:
#                 if nums[left] == 0:
#                     nums[left] = nums[right]
#                     nums[right] = 0
#                 left += 1
#                 right += 1
#             else:
#                 right += 1
