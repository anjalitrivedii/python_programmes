text = input("enter text: ").lower()
vowels = "aeiou"
vowel_count =sum(1 for c in text if c in vowels)
consonant_count = sum(1 for c in text if c.isalpha() and c not in vowels)
print("vowels:",vowel_count,"consonants:", consonant_count)