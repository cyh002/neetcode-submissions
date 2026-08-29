class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         # 1. avoid the sorting trap. use hash map / set O(1) in constant-time lookups
         # 2. only count those that are in the beginning 
         
         # pseudo code
         # setup
         # - use set to deduplicate
         # - initialize seen()
         # - max_count = 1
         # - for each i in num_set, and if it is not in seen:
            # - check if next = current + 1 in seen:
                # add current_count += 1
                # add the next in seen()
                # if current_count > max_count, assign max__count = current_count
            # else: 
                # reset count current_count == 0
                # contiue
         
        nums_set = set(nums)
        max_count = 0
        for num in nums_set:
            if (num - 1) not in nums_set: # start of the array
                current_num = num 
                curr_count = 1
                next_num = num + 1
                for _ in nums_set:
                    if next_num not in nums_set:
                        break
                    next_num += 1
                    curr_count += 1
                length = next_num - current_num
                if length > max_count:
                    max_count = length
        return max_count
                    


