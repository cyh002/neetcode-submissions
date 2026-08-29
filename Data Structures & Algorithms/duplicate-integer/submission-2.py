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
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
