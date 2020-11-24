'''
Time: O(m * n), m: matrix height, n: matrix width
Space: O(m * n), m: matrix height, n: matrix width
'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Recursion
        def pow(i, r):
            if i == 0:
                return 1
            if i % 2:
                return r * pow(i - 1, r)
            return pow(i / 2, r * r)
        result = pow(abs(n), x)

        # Iteration
        # if n == 0:
        #     return 1

        # i = abs(n)
        # result = 1
        # while i > 0:
        #     if i % 2:
        #         result *= x
        #     x *= x
        #     i //= 2

        if n < 0:
            return 1/result
        return result
