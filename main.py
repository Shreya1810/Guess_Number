import random
import time

print("Hi! Welcome to the guessing game. I am going to guess a number between 1 and 100.")
time.sleep(3)
print("Picking a number...")
time.sleep(3)
guess_num = int(input("What is your guess? "))
correct_num = random.randint(1,100)
guess_count = 0
while correct_num != guess_num:
  guess_count += 1
  if guess_num < correct_num:
    guess_num = int(input("Wrong You need to guess higher, What is your guess? "))

  else:
    guess_num = int(input("Wrong You need to guess lower, What is your guess? "))
  

print(f"Congrats! The right answer is {correct_num} , it took you {guess_count} guesses")