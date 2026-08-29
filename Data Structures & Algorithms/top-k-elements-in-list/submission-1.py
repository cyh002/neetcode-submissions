class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = Counter(nums)
        print(counted)
        print(counted.most_common(k))
        return [num for num, count in counted.most_common(k)] 