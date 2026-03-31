class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in '+-*/':
                b, a = int(stack.pop()), int(stack.pop())
                if t == '+': stack.append(a + b)
                if t == '-': stack.append(a - b)
                if t == '*': stack.append(a * b)
                if t == '/': stack.append(a / b)
            else: stack.append(t)
        
        return int(stack[0])