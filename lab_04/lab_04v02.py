def OperatorPriority(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

def IsOperator(c):
    return c in '+-*/^'

def InfixToPostfix(expression):
    output = []
    stack = []

    for char in expression:
        if char.isdigit() or char.isalpha(): 
            output.append(char)
        elif char == '(':  
            stack.append(char)
        elif char == ')':  
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop() 
        elif IsOperator(char): 
            while stack and OperatorPriority(stack[-1]) >= OperatorPriority(char):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

def EvaluatePostfix(expression):
    stack = []

    for char in expression:
        if char.isdigit(): 
            stack.append(int(char))
        elif IsOperator(char): 
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)
            elif char == '^':
                stack.append(a ** b)

    return stack[0] 

if __name__ == "__main__":
    infix_expr = input("Enter Expression: ").replace(' ', '')
    postfix_expr = InfixToPostfix(infix_expr)
    print(f"Reversed polish notation: {postfix_expr}")
    result = EvaluatePostfix(postfix_expr)
    print(f"Calculated result: {result}")