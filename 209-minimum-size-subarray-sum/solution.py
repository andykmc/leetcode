'''
Time: O(2n) = O(n): n :nums (each element can be visited twice)
Space: O(1): constant
*** s and nums are positive integrers
'''

# Solution 1 - with Time O(n)
import math


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        right = 0
        length = math.inf
        minSum = math.inf
        currSum = 0
        while right < len(nums):
            if currSum + nums[right] < s:
                currSum += nums[right]
                right += 1
            else:
                currSum -= nums[left]
                minSum = min(currSum, minSum)
                length = min(length, right - left + 1)
                left += 1
        return 0 if length == math.inf else length


# Solution 2 - with Time O(nlogn)
