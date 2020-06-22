'''
Time: O(n), n: nums
Space: O(1): constant
'''


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        rMax = 0
        currMax = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                currMax += 1
            else:
                rMax = max(currMax, rMax)
                currMax = 0
        return max(currMax, rMax)
