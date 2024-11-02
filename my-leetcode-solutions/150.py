class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operants = ['+', '-', '*', '/']
        stack = []
        i = 0
        
        while i < len(tokens):
            if tokens[i] not in operants:
                stack.append(int(tokens[i]))  
            else:
                a = stack.pop()  
                b = stack.pop()
                if tokens[i] == '+':
                    stack.append(b + a)
                elif tokens[i] == '-':
                    stack.append(b - a)
                elif tokens[i] == '*':
                    stack.append(b * a)
                elif tokens[i] == '/':
                    stack.append(int(b / a))
            i += 1
        
        return stack[0]

