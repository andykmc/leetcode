'''
Time: O(n), n: size of digits
Space: O(1): constant // not including input digits
'''


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in reversed(range(len(digits))):
            curr = digits[i]
            digits[i] = (curr + carry) % 10
            carry = (curr + carry) // 10

        if carry > 0:
            digits = [carry] + digits
        return digits
