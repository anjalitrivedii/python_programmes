import string
from inspect import cleandoc

text = input("enter text:")
clean_text="".join(c for c in text if c not in string.punctuation)
print("cleaned text:",clean_text)