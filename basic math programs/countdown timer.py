import time
n = int(input("enter countdown time in seconds:"))
while n > 0:
    print(n)
    time.sleep(1)
    n-=1
print("time's up!")