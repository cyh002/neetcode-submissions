class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count_set = set()
        left = 0
        max_n = 0
        
        for right in range(len(s)):
            # Shrink the window until the duplicate is gone
            while s[right] in count_set:
                count_set.remove(s[left])
                left += 1
            
            # Expand the window
            count_set.add(s[right])
            max_n = max(max_n, right - left + 1)
            
        return max_n