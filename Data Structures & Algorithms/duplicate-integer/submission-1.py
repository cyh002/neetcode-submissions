class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_list = sorted(nums)
        results = [curr == prev for prev, curr in zip(sorted_list[:], sorted_list[1:])]
        if True in results:
            return True
        else:
            return False
    
