class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # # hash map
        
        # find the balance
        seen =  {}
        for i, current in enumerate(nums):
            balance = target - current
            # check if balance is in the seen:
            if balance in seen:
                balance_index = seen[balance]
                return [balance_index, i]
            seen[current] = i