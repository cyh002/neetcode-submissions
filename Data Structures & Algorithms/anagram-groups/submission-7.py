from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ordered_str = []
        results_dict = defaultdict(list)
        for word in strs:
            ordered_word_list = sorted(word)
            ordered_word = "".join(ordered_word_list)
            ordered_str.append(ordered_word)
        zipped = list(zip(ordered_str,strs))
        for item in zipped:
            results_dict[item[0]].append(item[1])
        return list(results_dict.values())
        
            