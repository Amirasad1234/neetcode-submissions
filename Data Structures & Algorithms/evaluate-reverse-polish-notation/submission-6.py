class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        arithm = ['-', '*', '/', '+']
        for i in range(len(tokens)):
            if tokens[i] not in arithm:
                stack.append(int(tokens[i]))
            else:
                if tokens[i] == '+':
                    res = stack.pop() + stack.pop()
                if tokens[i] == '-':
                    a, b = stack.pop(), stack.pop()
                    res = b - a    
                if tokens[i] == '*':
                    res = stack.pop() * stack.pop()
                if tokens[i] == '/':
                    a, b = stack.pop(), stack.pop()
                    res = b / a
                stack.append(int(res))
        return stack[-1]


