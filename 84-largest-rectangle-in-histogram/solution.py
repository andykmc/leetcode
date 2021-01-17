# Time: O(N log(N))
# Space: O(N)

# Note that the node in segment tree used here is used to store the index of minimal value of the historgram,
# instead of the value isself.
class STNode:
    def __init__(self, minIndex, left=None, right=None, start=None, end=None):
        self.min = minIndex
        self.left = left
        self.right = right
        self.start = start
        self.end = end


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        if not heights:
            return maxArea

        if len(heights) == 1:
            return heights[0]

        def genST(start, end):
            if start == end:
                return STNode(start, None, None, start, end)

            mid = (start + end) // 2
            left = genST(start, mid)
            right = genST(mid + 1, end)
            return STNode(left.min if heights[left.min] <= heights[right.min] else right.min, left, right, left.start, right.end)

        st = genST(0, len(heights) - 1)

        def searchST(start, end, st):
            if st.start >= start and st.end <= end:
                return st.min
            if st.start > end or st.end < start:
                return None
            leftIndex = searchST(start, end, st.left)
            rightIndex = searchST(start, end, st.right)

            if leftIndex is None:
                return rightIndex
            if rightIndex is None:
                return leftIndex
            return leftIndex if heights[leftIndex] <= heights[rightIndex] else rightIndex

        def maxArea(start, end, st):
            if start > end:
                return -math.inf
            if start == end:
                return heights[start]

            minIndex = searchST(start, end, st)
            leftArea = maxArea(start, minIndex - 1, st)
            rightArea = maxArea(minIndex + 1, end, st)
            thisArea = (end - start + 1) * heights[minIndex]

            calMaxArea = max(thisArea,
                             leftArea,
                             rightArea)

            return calMaxArea

        return maxArea(0, len(heights) - 1, st)
