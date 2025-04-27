nums = list(map(int,input("enter numbers:").split()))
for i in range(len(nums)):
    for j in range(i + 1 ,len(nums)):
        if nums[i]>nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
print("sorted list:",nums)