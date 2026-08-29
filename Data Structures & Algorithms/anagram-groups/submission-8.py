from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results_dict = defaultdict(list)
        for word in strs:
            ordered_word = "".join(sorted(word))
            results_dict[ordered_word].append(word)
        return list(results_dict.values())
            