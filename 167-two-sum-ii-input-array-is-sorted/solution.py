'''
Time: O(n), n: numbers
Space: O(1): constant
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] > target:
                right -= 1
                left = 0
            else:
                left += 1

        return [left + 1, right + 1]
