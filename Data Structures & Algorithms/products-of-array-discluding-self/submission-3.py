import math
class Solution:
    # Key Learning:
    # - Split a Total Result into Left and Right Components
    # - find a way to cache previous resuls

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
    
    # # O(n^2) still bad
    # def productExceptSelf(self, nums:List[int]) -> List[int]:
    #     prefix = 1
    #     result = []
    #     for i, val in enumerate(nums):
    #         suffix =  math.prod(nums[i+1:])
    #         product = prefix * suffix
    #         result.append(product)
    #         prefix *= val
    #     return result
    

