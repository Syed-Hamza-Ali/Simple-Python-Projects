# Number Guessing Game
import random
n=random.randint(1,500)
user_input=int(input("Guess the number : "))
num_guess=0
while n!=user_input:
    if n<user_input:
        print("Guess Lower")
        user_input = int(input("Guess the number : "))
        num_guess+=1
    if n>user_input:
        print("Guess Higher")
        user_input = int(input("Guess the number : "))
        num_guess+=1
print("*.*.*.Correct.*.*.*")
print("Number of guesses : ",num_guess)
