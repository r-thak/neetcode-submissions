class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False
        stack = []

        for i in range(len(s)):
            c = s[i]
            if len(stack) > 0: t = stack[len(stack) - 1]
            else: t = False

            if c == '(' or c == '{' or c == '[':
                stack.append(c)
                continue
            if t == False: return False
            if t == '(' and c != ')' or t == '{' and c != '}' or t == '[' and c != ']': return False
            stack.pop()
        if len(stack) != 0: return False
        return True