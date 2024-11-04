import random

rps = ["rock", "paper", "scissors"]
win = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}
guess = input("Choose rock, paper, or scissors: ").lower()

parameter = random.choice(rps)
print(f"Computer chose: {parameter}")

if guess == parameter:
    print("It's a tie!")
elif win[guess] == parameter:
    print("You win!")
else:
    print("You lose!")