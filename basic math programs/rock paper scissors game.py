import random
choices = ["rock","paper","scissors"]
user = input("enter rock/paper/scissors:").lower()
comp = random.choice(choices)
print("computer chose:",comp)
if user == comp:
    print("draw")
elif(user == "rock" and comp == "scissors")or(user == "paper") or (user == "scissor" and comp == "paper"):
    print("you win!")
else:
    print("you lose!")