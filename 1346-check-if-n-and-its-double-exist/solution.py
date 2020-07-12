'''
Space: O(n)
Time: O(nlogn)
'''


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        myMap = {}
        arr.sort(reverse=True)
        for a in arr:
            if a * 2 in myMap:
                return True
            else:
                myMap[a] = True
        arr.reverse()
        myMap = {}
        for a in arr:
            if a * 2 in myMap:
                return True
            else:
                myMap[a] = True
        return False
