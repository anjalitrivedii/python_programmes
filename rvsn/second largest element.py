from enum import unique


def second_largest(lst):
    unique = set(lst)
    if len(unique)<2:
        return None
    unique.remove(max(unique))
    return max(unique)
numbers =[10, 20, 4, 45, 99]
print("Second Largest:",second_largest(numbers))