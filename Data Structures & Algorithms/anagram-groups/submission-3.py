from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def check_anagrams(first_word: str, second_word: str):
                return Counter(first_word) == Counter(second_word)
        visited = set()
        length = len(strs)
        results = []
        for i, current_word in enumerate(strs): # 0, act
            if i in visited: # false
                continue
            sublist = [] # empty list
            sublist.append(current_word) # ["act"]
            for j in range(i+1, length): #
                if j not in visited and check_anagrams(strs[j],current_word):
                    sublist.append(strs[j])
                    visited.add(j)
            results.append(sublist)
        return results
                