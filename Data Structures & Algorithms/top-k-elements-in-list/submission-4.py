class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counted = Counter(nums)
        # return [k for k, v in counted.most_common(k)]

        # Brute Force
        distinct_num = set(nums)
        results = defaultdict(int)
        for num in nums:
            results[num] += 1
        ordered = list(results.items())
        ordered.sort(key=lambda x: x[1], reverse=True)
        return [num for num, count in ordered[:k]]

            