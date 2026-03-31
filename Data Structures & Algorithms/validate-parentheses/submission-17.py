class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
                continue
            
            if not stack and c in ')}]': return False
            peek = stack[len(stack) - 1]

            if c == ')' and peek == '(' or c == '}' and peek == '{' or c == ']' and peek == '[':
                stack.pop()
            else: return False

        if stack: return False
        return True