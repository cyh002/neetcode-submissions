import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 1. nums must be bigger than k 
        # if len(nums) < k:
        #     return []
        results = []

        # Brute Force O(n^2)
        # for num_idx in range(len(nums)): 
        #     if not num_idx + k > len(nums): # Outer loop : O(n * k)
        #         window = nums[num_idx:num_idx + k] # O(k))
        #         max_num = max(window) # O(k)
        #         results.append(max_num)
        # return results

        # Sliding Window
        heap = []
        for i in range(len(nums)): # 2
            # print(f"iter: {i}")
            heapq.heappush(heap, (-nums[i], i))
            # the top now gets the highest in the heap
            if i >= k - 1: # if the index is greater k , we need to start caring about removing the index that fell out of window
                while heap and i - heap[0][1] >= k: # if i = 5, we are concerned about [3,4,5], if max_heap_idx = 2, 5-2 = 3
                    heapq.heappop(heap)
                result = -heap[0][0]
                # print(f"iter__if_result:{result}")
                results.append(-heap[0][0])
                # print(f"heap: {-heap[0][0]}")
        return results

            


            



