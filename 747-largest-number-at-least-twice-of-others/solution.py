'''
Space: O(1)
Time: O(n)
'''


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = 0
        larger = 0
        index = 0
        for i, num in enumerate(nums):
            if num > largest:
                index = i
                larger = largest
                largest = num
            elif num > larger:
                larger = num
        if largest >= larger * 2:
            return index
        return -1
