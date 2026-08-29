class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute Force
        # Generate every possible option
        n = len(s)
        max_length = 0
        # for i in range(n):
        #     seen = set()
        #     for j in range(i, n):
        #         if s[j] in seen:
        #             break
        #         seen.add(s[j])
        #         current_length = j - i + 1
        #         max_length = max(current_length, max_length)
        # return max_length
        
        # Sliding Window
        left = 0 
        last_seen = {}
        # Last seen is used to track for every character the last position, so we can retire any thing else before that. 
        for right in range(n):
            char = s[right]
            # if the character has been seen and the character is in the window, we need to shift the left pointer forward to skip it
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1 # skip it
            # we need to assign the char the postion in which it is seen
            last_seen[char] = right
            max_length = max(max_length, right - left + 1)
        return max_length 

        # Dynamic Programming