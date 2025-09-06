#method 1
# def reverse_string(s):
#     return s[::-1]
# print(reverse_string("hello"))

#method 2
text = "hello"
reversed_text = "".join(reversed(text))
print(reversed_text)

#method 3
text = ("hello")
reversed_text = ''.join(list(reversed(text)))
print(reversed_text)