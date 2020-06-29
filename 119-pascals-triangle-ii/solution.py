'''
Time: O(k^2), k: rowIndex
Space: O(k), k: rowIndex
'''


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1] * (rowIndex + 1)
        for i in range(rowIndex + 1):
            for j in reversed(range(1, i)):
                result[j] += result[j - 1]
        return result
