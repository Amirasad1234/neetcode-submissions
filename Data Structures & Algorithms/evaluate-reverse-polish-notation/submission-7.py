class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sign = '+-*/'
        stack = []
        res = 0
        for i in range(len(tokens)):
            if tokens[i] in sign:
                first = stack.pop()
                second = stack.pop()
                if tokens[i] == '+':
                    stack.append(first + second)
                if tokens[i] == '-':
                    stack.append(second - first)
                if tokens[i] == '*':
                    stack.append(first * second)
                if tokens[i] == '/':
                    stack.append(int(second / first))
            else:
                stack.append(int(tokens[i]))
        return stack[-1]
        
        
        
            
        


        