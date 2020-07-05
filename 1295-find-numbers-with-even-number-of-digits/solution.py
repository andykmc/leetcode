'''
Space: O(1)
Time: O(n)
'''

import math


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            if int(math.log10(n)) % 2 == 1:
                count += 1
        return count
