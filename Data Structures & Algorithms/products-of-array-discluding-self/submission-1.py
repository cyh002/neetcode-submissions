class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def multiply_all(nums_list: List[int]) -> int:
            nums_list_sorted = sorted(nums_list)
            result = nums_list_sorted[0]
            for num in nums_list_sorted[1:]:
                result *= num
            return result
        result = []
        for i, val in enumerate(nums):
            balance = multiply_all(nums[:i] + nums[i+1:])
            result.append(balance)
        return result