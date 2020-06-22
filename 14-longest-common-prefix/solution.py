'''
Time: O(min(strs))
Space: O(1): constant
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        words = len(strs)
        if words == 0:
            return ''
        if words == 1:
            return strs[0]
        prefix = ''
        i = 0
        while True:
            for w in range(words):
                if strs[w] == '' or i == len(strs[w]):
                    return prefix
                if w == 0:
                    curr = strs[w][i]
                else:
                    if curr != strs[w][i]:
                        return prefix
            prefix += curr
            i += 1
        return prefix
