def are_anagrams(s1,s2):
    return sorted(s1) == sorted(s2)
str1 = "race"
str2 ="care"
print(are_anagrams(str1,str2))