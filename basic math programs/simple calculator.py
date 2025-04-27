a = float(input("enter first number:"))
b = float(input("enter second number:"))
op=input("enter operation(+,-,*,/):")
if op =='+':
    print("Result:",a + b)
elif op =='-':
    print("Result:",a - b)
elif op =='*':
    print("Result:",a * b)
elif op =='/':
    if b !=0:
        print("Result:",a / b)
    else:
        print("cannot  divide by zero!")
else:
        print("invalid operator.")