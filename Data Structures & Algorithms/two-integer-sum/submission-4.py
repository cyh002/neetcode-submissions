class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force
        # n = len(nums)
        # for i in range(n):
        #    for j in range(i + 1, n):
        #        if nums[i] + nums[j] == target:
        #            return [i, j]
        
        # Difference Arrays
        n = len(nums)
        seen = {}
        for i in range(n):
            balance = target - nums[i]
            if balance in seen:
                return [seen[balance], i]
            seen[nums[i]] = i
            