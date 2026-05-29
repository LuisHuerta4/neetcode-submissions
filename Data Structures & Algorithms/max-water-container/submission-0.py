class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        length = len(heights)
        for i, left_height in enumerate(heights):
            for j, right_height in enumerate(heights[i + 1:], start = i + 1):
                area = min(left_height, right_height) * (j - i)
                #print(f"left: {left_height}, right: {right_height}, area: {area} (i = {i}, j = {j})")
                if area > max_area:
                    max_area = area

        return max_area