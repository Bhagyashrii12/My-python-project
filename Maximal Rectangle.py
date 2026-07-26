class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        maxArea = 0

        for row in matrix:
            # Update heights
            for i in range(cols):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0

            # Largest Rectangle in Histogram
            stack = []
            h = heights + [0]

            for i in range(len(h)):
                while stack and h[stack[-1]] > h[i]:
                    height = h[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    maxArea = max(maxArea, height * width)
                stack.append(i)

        return maxArea
