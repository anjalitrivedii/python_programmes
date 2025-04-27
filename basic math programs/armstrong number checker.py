num = int(input("enter a number:"))
power = len(str(num))
total = sum(int(digit) ** power for digit in str(num))
if total == num:
    print("armstrong number")
else:
    print("not an armstrong number")