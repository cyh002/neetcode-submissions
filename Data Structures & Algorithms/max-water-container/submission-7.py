class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute Force
        # length = len(heights)
        # max_water = 0
        # for i in range(length):
        #     for j in range(i, length):
        #         calc_water = min(heights[i], heights[j]) * (j - i)
        #         max_water = max(calc_water, max_water)
        # return max_water

        # Two Pointers
        # you move if in the direction if the side with the lesser
        length = len(heights)
        max_water = 0 
        right = length -1
        left = 0 
        while right > left:
            min_height = min(heights[left], heights[right])
            area = min_height * (right - left)
            max_water = max(area, max_water)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_water
            
            

