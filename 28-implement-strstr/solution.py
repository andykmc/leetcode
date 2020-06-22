'''
Time: O(n), n: haystak
Space: O(1): constant
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        left = 0
        while left + len(needle) <= len(haystack):
            if haystack[left:left+len(needle)] == needle:
                return left
            left += 1
        return -1
