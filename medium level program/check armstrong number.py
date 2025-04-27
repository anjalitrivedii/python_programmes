def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d)**power for d in digits)
print(is_armstrong(153)) #true
print(is_armstrong(123)) #false