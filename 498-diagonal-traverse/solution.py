'''
Time: O(matrix)
Space: O(matrix)
'''


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if len(matrix) == 0:
            return []

        for i in range(1, len(matrix[0]) + 1):
            j = 0
            temp = []
            for currI in reversed(range(i)):
                temp.append(matrix[j][currI])
                j += 1
                if j >= len(matrix):
                    break
            result.append(temp)

        for j in range(1, len(matrix)):
            temp = []
            i = len(matrix[0]) - 1
            for currJ in range(j, len(matrix)):
                temp.append(matrix[currJ][i])
                i -= 1
                if i < 0:
                    break
            result.append(temp)

        result2 = []
        for r in range(len(result)):
            if r % 2 == 0:
                result[r].reverse()
            result2 += result[r]

        return result2
