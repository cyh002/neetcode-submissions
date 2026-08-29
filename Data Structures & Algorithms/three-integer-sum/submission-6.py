class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums_sorted = sorted(nums)
        results = []
        for i in range(length):
            search_space = nums_sorted[i+1:]
            target = nums_sorted[i]
            left , right = 0, len(search_space) - 1   
            while right > left: 
                current_sum = search_space[right] + search_space[left]
                if current_sum == -target:
                    results.append([target, search_space[left], search_space[right]])
                if -target > current_sum:
                    left += 1
                else:
                    right -= 1
        return [list(x) for x in {tuple(x) for x in results}]
