'''
Time: O(n), n: nums
Space: O(1)
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        while right < len(nums):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
                right += 1
            else:
                right += 1
        return left + 1
