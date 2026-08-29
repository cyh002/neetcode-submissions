from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for each in strs:
            ordered = "".join(sorted(each))
            results[ordered].append(each)
        return list(results.values())
