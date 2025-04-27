from enum import unique

nums = list(map(int,input("enter numbers:").split()))
freq = {}
for num in nums:
    freq[num] = freq.get(num,0)+1
print("frequencies:",freq)