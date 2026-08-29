from typing import Generator
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # My Solution:
        # - no early exit
        # - redudant logic : return True in results
        # - creates 4 memory list
        #   - sorted_list
        #   - sorted_list[1:]
        #   - sorted_list[:]
        #   - results[:]

        # sorted_list = sorted(nums)
        # results = [curr == prev for prev, curr in zip(sorted_list[:], sorted_list[1:])]
        # if True in results:
        #     return True
        # else:
        #     return False
        
        # Hash Set 
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False

        # Generator function
        # nums.sort()
        # generator = (nums[i] == nums[i-1] for i in range(1, len(nums)))
        # return any(generator)
    
        # hash way
        # seen = set()
        # for i in range(len(nums)):
        #     current_num = nums[i]
        #     if current_num in seen:
        #         return True
        #     seen.add(current_num)
        # return False

        # generator
        nums.sort()
        # create the generator that compares between two numbers the current and the previous and return true or false
        generator = (nums[i] == nums[i-1] for i in range(1, len(nums)))
        return any(generator)
            