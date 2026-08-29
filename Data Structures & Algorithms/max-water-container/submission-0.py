class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Formula
        def area(heights: List[int], first_index: int, last_index:int ):
            # min(first_value, last_value) * (last_index - first_index)
            first_value = heights[first_index]
            last_value = heights[last_index]
            return min(first_value, last_value) * (last_index - first_index)
        # Brute Force Way:
        length = len(heights) 
        max_area = 0
        for i in range(length):
            for j in range(i+1, length):
                current_area = area(heights, i, j)
                if current_area > max_area:
                    max_area = current_area
        return max_area
        