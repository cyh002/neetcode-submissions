class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force
        # length = len(nums)
        # for i in range(length):
        #     for j in range(1, length+1):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # Hashmap-uh
        seen = {}
        for index,current in enumerate(nums):
            balance = target - current
            if balance in seen.keys():
                return [seen[balance],index]
            seen[current] = index