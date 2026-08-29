class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Formula
        def area(heights: List[int], first_index: int, last_index:int ):
            # min(first_value, last_value) * (last_index - first_index)
            first_value = heights[first_index]
            last_value = heights[last_index]
            return min(first_value, last_value) * (last_index - first_index)
        length = len(heights)
        max_area = 0 
        # # Brute Force Way:
        # for i in range(length):
        #     for j in range(i+1, length):
        #         current_area = area(heights, i, j)
        #         if current_area > max_area:
        #             max_area = current_area
        # return max_area
        left, right = 0, len(heights) - 1
        while left < right: 
            current_area = area(heights, left, right)
            if current_area > max_area:
                max_area = current_area
            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1
        return max_area


        