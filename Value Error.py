# Safe Number Input Checker
# File  : safe_input.py

print("====================================")
print("      Welcome to Safe Input!        ")
print("====================================")
print()

# Using a while loop with try-except to handle errors gracefully
while True:
    try:
        number = int(input("Enter an integer number: "))
        print()
        print(f"Success! The number entered is: {number}")
        print("-" * 36)
        break  # Exit the loop once valid input is provided
        
    except ValueError as ex:
        print()
        print(f"Oops! Invalid input. Exception: {ex}")
        print("Please try again with a valid whole number.\n")

print()
print("====================================")
print("   Program completed successfully! 🛡️ ")
print("====================================")