import random
num = random.randint(0,10)
print("Guess the random number between 0 and 10")
while True:
   guess = int(input("Your guess: "))
   if guess == num:
      print("Congrats! You guessed correctly!")
      break
   elif guess > num:
      print("Too high! Try again!")
   else:
      print("Too low! Try again!")