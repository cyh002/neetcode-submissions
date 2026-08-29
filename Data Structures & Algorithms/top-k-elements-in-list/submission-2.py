class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counted = Counter(nums)
        return [k for k, v in nums_counted.most_common(k)]