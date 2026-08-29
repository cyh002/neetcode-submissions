class Solution:
    def trap(self, height: List[int]) -> int:
        # Need to calculate MaxToRight and MaxToLeft
        MaxToRight = MaxToLeft = 0
        MaxToRight_list, MaxToLeft_list = [], []
        length = len(height)
        topwater_list = []
        def calculate_topwater(current_height, MaxToRight, MaxToLeft):
            return min(MaxToRight, MaxToLeft) - current_height
        for i in range(length):
            # Update MaxToRight
            if height[i] > MaxToRight:
                MaxToRight = height[i]
            MaxToRight_list.append(MaxToRight)
            if height[length - 1 - i] > MaxToLeft:
                MaxToLeft = height[length - 1 - i]
            MaxToLeft_list.append(MaxToLeft)
        MaxToLeft_list.reverse()
        topwater_list = [
    calculate_topwater(height[i], MaxToRight_list[i], MaxToLeft_list[i]) for i in range(length)
]
        return sum(topwater_list)
        