class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                # left side is sorted
                if nums[mid] > target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # right side is sorted
                if nums[right] >= target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        
        # if i am searching for 4: 
        # [3, 4, 5, 6, 1, 2]
        # left is sorted.
        # target falls into the sorted left side
        # find the target in the sorted left. 


        # [5, 6, 7, 8, 4, 5]
        # left is sorted
        # target does not fall into the sorted left side 
        # 

        # [16, 4, 5, 8, 10, 15]


        # Strategy: 
        # take mid
        # check if left is sorted: 
            # if yes
                # target lies in the boundary - use sorted_search. 
                # target lies out of the boundary - then use right side
            # then right is sorted