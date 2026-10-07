from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = Counter(nums)
        counted_list = sorted(counted.items(), key = lambda item : item[1], reverse = True)
        counted_list = [item[0] for item in counted_list]
        return counted_list[:k]