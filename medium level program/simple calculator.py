def calculator(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b if b!= 0 else 'cannot divide by zero'


print(calculator(10, 5, '+'))  # 15
print(calculator(10,5,'/')) #2.0