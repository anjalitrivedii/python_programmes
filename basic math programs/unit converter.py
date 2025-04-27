value = float(input("enter value:"))
unit = input("convert(cm->in/in->cm):").lower()
if unit == "cm->in":
    print("in inches:",value / 2.54)
elif unit == "in cm:":
    print("in cm:",value *2.54)
else:
    print("invalid conversion")