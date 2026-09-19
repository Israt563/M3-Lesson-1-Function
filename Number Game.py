# Number Guessing Game
# File  : guessing_game.py

import random

print("====================================")
print("     Welcome to Number Guessing!    ")
print("====================================")
print()

# Initialize game variables
number = str(random.randint(0, 9))
attempts = 0

print("I have generated a random digit from 0 to 9.")
print("Can you guess what it is? Let's play! 🎲")
print("-" * 36)
print()

# Iterate loop until the user guesses correctly
while True:
    guess = input("Give me your best guess (0-9): ").strip()
    attempts += 1
    print()
    
    if number == guess:
        print("🎉 You win the game!")
        print(f"The hidden number was : {number}")
        print(f"Total attempts taken  : {attempts}")
        break
    else:
        print("❌ Your guess isn't quite right, try again.\n")

print()
print("====================================")
print("   Game over. Thanks for playing! 🎮")
print("====================================")