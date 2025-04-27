def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join([ch for ch in s if ch not in vowels])
print(remove_vowels("Programming"))