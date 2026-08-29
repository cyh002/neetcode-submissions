class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # define formula: 
        def formula(heights, start_idx, end_idx):
            return min(heights[start_idx], heights[end_idx]) * (
                end_idx - start_idx
            )
        max_result = 0
        length = len(heights)
        # Brute Force
        # for i in range(length):
        #     for j in range(i+1, length):
        #         current = formula(heights, i, j)
        #         if current > max_result:
        #             max_result = current
        #         # print(i, j)
        # return max_result
        
        # Two Pointers
        left , right = 0, length - 1
        # What is the decision to decide if to move right or to move left ?
        # we move the opposite direction of the min (left, right)
        while right > left:
            current = formula(heights, left, right)
            if current > max_result:
                max_result = current
            if heights[left] < heights[right]:
                left += 1 
            else:
                right -=1
        return max_result

