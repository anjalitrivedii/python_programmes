def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
print(is_number("123.45"))  #True
print(is_number("abc"))  #False