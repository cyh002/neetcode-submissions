class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = s.lower().split()
        word_list = list("".join(words))
        cleaned_list = [ss for ss in word_list if ss.isalnum()]
        print(cleaned_list.reverse())
        return cleaned_list == cleaned_list[::-1]