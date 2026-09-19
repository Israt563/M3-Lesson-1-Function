# Cube and Divisibility Checker
# File  : cube_checker.py

print("====================================")
print("      Welcome to Cube Checker!      ")
print("====================================")
print()

# Define function to calculate cube
def cube(number):
    return number * number * number
  
# Define a function which will execute cube function if the user entered number is divisible by 3
def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

# Display results for predefined tests
print("--- Running Test Cases ---")
print(f"Testing 9 -> {by_three(9)}")
print(f"Testing 4 -> {by_three(4)}")
print("-" * 36)
print()

# Interactive user test
user_input = int(input("Enter your own number to test: "))
print()

result = by_three(user_input)

print("====================================")
print("========== TEST RESULT =============")
print("====================================")
if result is not False:
    print(f"Success! {user_input} is divisible by 3.")
    print(f"Its cube is        : {result}")
else:
    print(f"Oops! {user_input} is NOT divisible by 3.")
    print(f"Returned           : {result}")
print("====================================")