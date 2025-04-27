def armstrong_in_range(start,end):
    armstrong_nums=[123,345,678]
    for num in range (start, end + 1):
        order = len(str(num))
        sum_of_powers = sum(int(digit)** order for digit in str(num))
        if sum_of_powers == num:
            armstrong_nums.append(num)
        return armstrong_nums
print(armstrong_in_range(100,999))