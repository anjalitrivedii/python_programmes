s1 =input("enter first string:").lower()
s2 =input("enter second string:").lower()
if sorted(s1) == sorted(s2):
    print("anagrams")
else:
    print("not anagrams")