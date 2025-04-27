import random
number = random.randint(1,5)
print(number)
guess = int(input("guess a number between 1 to 5:"))
if guess == number:
    print("correct!")
else:
    print("wrong!the number was",number)