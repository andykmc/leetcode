'''
Time: O(numRows^2)
Space: O(numRows^2)
'''


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for row in range(numRows):
            if row == 0:
                result.append([1])
            else:
                resultRow = [1]
                for i in range(1, row):
                    resultRow.append(result[-1][i - 1] + result[-1][i])
                resultRow.append(1)
                result.append(resultRow)
        return result
