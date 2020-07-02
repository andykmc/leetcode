'''
Time: O(n), n: s
Space: O(n), n: s
'''


class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s.split())
        for i in range(len(s)):
            s[i] = s[i][::-1]
        return ' '.join(s)
