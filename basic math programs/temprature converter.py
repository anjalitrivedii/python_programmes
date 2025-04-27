temp = float(input("enter temprature:"))
unit = input("convert to (C/F):").upper()
if unit == "C":
    print("in celcius:", (temp - 32) * 5 / 9)
elif unit == "F":
    print("in fahrenheit:", (temp * 9 / 5) + 32)
else:
    print("invalid unit")
