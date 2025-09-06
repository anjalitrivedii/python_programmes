def linear_search(lst,target):
    for i ,val in enumerate(lst):
        if val == target:
            return i
        return -1
num = [10,25,30,45,50]
x = 45
print(linear_search(num,x))