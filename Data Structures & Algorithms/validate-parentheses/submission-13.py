class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if stack and char in [')',']','}']:
                if char ==')' and stack[-1] == '(':
                    stack.pop()
                    continue
                elif char ==']' and stack[-1] == '[':
                    stack.pop()
                    continue
                elif char =='}' and stack[-1] == '{':
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(char)
        return False if stack else True

        
        