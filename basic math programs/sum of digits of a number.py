from unicodedata import digit

num = input("enter a number:")
sum_digits = sum(int(digit)for digit in num)
print("sum of digits:",sum_digits)