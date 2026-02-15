import random
print("Welcome to the Number Guessing Game!")
number = random.randint(1, 10)
guess = input("Guess the number between 1 and 10: ")
if int(guess) == number:    
 print("Correct! You win!")
else:
 print("Wrong! The number was " + str(number))