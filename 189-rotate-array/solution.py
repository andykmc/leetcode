# Solution 3
# Space: O(1)
# Time: O(n), n: nums
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l, start, end):
            left = start
            right = end
            while (left < right):
                temp = l[right]
                l[right] = l[left]
                l[left] = temp
                left += 1
                right -= 1

        modK = k % len(nums)

        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, modK - 1)
        reverse(nums, modK, len(nums) - 1)


# Solution 2
# Space: O(1)
# Time: O(k*nums)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        modK = k % len(nums)
        for i in range(modK):
            temp = nums[-1]
            del nums[-1]
            nums[:0] = [temp]


# Solution 1
# Space: O(nums)
# Time: O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        modK = k % len(nums)
        temp = nums[(-1 * modK):]
        del nums[(-1 * modK):]
        nums[:0] = temp
