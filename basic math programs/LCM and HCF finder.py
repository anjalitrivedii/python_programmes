import math

a = int(input("enter first number:"))
b = int(input("enter second number:"))
print("HCF:",math.gcd(a,b))
lcm = abs(a*b )// math.gcd(a,b)
print("LCM:",lcm)