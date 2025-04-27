def is_leap_year(year):
    if (year%4 == 0 and year%100 !=0) or (year%100 == 0):
        return True
    return False
print(is_leap_year(2024))  #True
print(is_leap_year(2023))  #False