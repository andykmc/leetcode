'''
Time: O(m * n), m: matrix height, n: matrix width
Space: O(m * n), m: matrix height, n: matrix width
'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        minCol = 0
        maxCol = len(matrix[0]) - 1
        minRow = 0
        maxRow = len(matrix) - 1
        result = []

        while minCol <= maxCol and minRow <= maxRow:
            for col in range(minCol, maxCol + 1):
                result.append(matrix[minRow][col])
            minRow += 1
            for row in range(minRow, maxRow + 1):
                result.append(matrix[row][maxCol])
            maxCol -= 1
            if minRow <= maxRow:
                for col in reversed(range(minCol, maxCol + 1)):
                    result.append(matrix[maxRow][col])
                maxRow -= 1
            if minCol <= maxCol:
                for row in reversed(range(minRow, maxRow + 1)):
                    result.append(matrix[row][minCol])
                minCol += 1
        return result
