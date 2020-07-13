'''
Space: O(1)
Time: O(n)
'''


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        localMax = 1
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
                localMax = max(arr[i], localMax)
                arr[i] = -1
            else:
                temp = arr[i]
                arr[i] = localMax
                localMax = max(temp, localMax)

        return arr
