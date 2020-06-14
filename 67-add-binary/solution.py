'''
Time: O(A + B, max(A, B))
Space: O(A + B)
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = ''
        while i >= 0 or j >= 0 or carry:
            sum = 0
            if i >= 0:
                sum += int(int(a[i]))
                i -= 1
            if j >= 0:
                sum += int(int(b[j]))
                j -= 1
            sum += carry
            carry = sum // 2
            sum %= 2
            result = str(sum) + result

        return result
