class Solution:
    def findMin(self, nums: List[int]) -> int:
        # two questions. 
        # 1. how do i know when to go left or right? 
        # 2. howw do i know if that is the breaking point? 

        # if last > first, then no issues: 
        first = nums[0]
        last = nums[-1]
        if last > first:
            return first
        # basically find the breakage point when it is the last.
        n = len(nums)
        left = 0 
        right = n - 1
        while right > left:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
            
        