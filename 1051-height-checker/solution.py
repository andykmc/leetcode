'''
Space: O(n)
Time: O(n)
'''


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = sorted(heights)
        count = 0
        for i in range(len(temp)):
            if temp[i] != heights[i]:
                count += 1
        return count
