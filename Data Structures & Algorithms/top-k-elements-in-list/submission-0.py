from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counted = Counter(nums)
        most_common_values = nums_counted.most_common(k)
        result = [pair[0] for pair in most_common_values]
        return result