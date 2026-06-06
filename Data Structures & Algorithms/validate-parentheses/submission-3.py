class Solution:
    def isValid(self, s: str) -> bool:
        opening = {'(', '[', '{'}
        closing = {')', ']', '}'}
        stack = []
        # Add opening brackets to stack
        # closing bracket = pop opening bracket off stack
        # not same type bracket means invalid
        # Non empty stack at end means invalid
        # else valid

        if len(s) == 1:
            return False

        for c in s:
            if c in opening:
                stack.append(c)
            else:
                if not stack: return False
                elif c == ')' and stack[-1] != '(': return False
                elif c == '}' and stack[-1] != '{': return False
                elif c == ']' and stack[-1] != '[': return False
                stack.pop()
        
        if not stack: return True
        return False