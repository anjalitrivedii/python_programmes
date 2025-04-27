from enum import nonmember


def add(x,y):
    return (x+y)
def sub(x,y):
    return(x-y)
def mul(x,y):
    return(x*y)
def div(x,y):
    if y !=0:
        return x / y
    else:
        return"cannot divide by zero"

num1 =float(input("enter first number:"))
num2 =float(input("enter second number:"))
operation = input("enter operation(+,-,*,/):")
result =None

if operation =='+':
    result = add(num1,num2)
elif operation =='-':
    result = sub(num1,num2)
elif operation=='*':
    result = mul(num1,num2)
elif operation == '/':
    result = div(num1,num2)
else:
    print("invalid operation")

if result is not None:
    print(f"Result:{result}")


