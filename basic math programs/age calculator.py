birth_year = int(input("enter birth year:"))
from datetime import datetime
Current_year = datetime.now().year
print("your age is:",Current_year-birth_year)