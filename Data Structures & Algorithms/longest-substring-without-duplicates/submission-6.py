class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        count_set = set()
        substr = []
        max_n = 0
        for char in s:
            while char in count_set:
                count_set.remove(substr[0])
                substr.pop(0)
            count_set.add(char)
            substr.append(char)
            max_n = max(len(substr), max_n)
        return max_n
            
