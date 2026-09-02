class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi =  0, len(nums) - 1
        while hi >= lo:
            mid = (hi + lo)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi -= 1
            else:
                lo += 1
        return -1