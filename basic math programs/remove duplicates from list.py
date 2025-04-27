nums = list(map(int,input("enter numbers:").split()))
unique = []
for num in nums:
    if num not in unique:
        unique.append(num)
print("without duplicates:",unique)