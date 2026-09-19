# Recursive Factorial Calculator
# File  : recursive_factorial.py

print("====================================")
print("   Welcome to Factorial Explorer!   ")
print("====================================")
print()

def factorial(x):
    '''This is a recursive function to find the factorial of an integer'''
    if x < 0:
        return "Factorial is not defined for negative numbers."
    elif x == 0 or x == 1:
        return 1
    else:
        # Calling function inside a function (recursion)
        return x * factorial(x - 1)

# Display function docstring
print("--- Function Docstring ---")
print(factorial.__doc__)
print()

# Display preset test results
print("--- Preset Test Results ---")
print(f"The factorial of 0 : {factorial(0)}")
print(f"The factorial of 1 : {factorial(1)}")
print(f"The factorial of 2 : {factorial(2)}")
print(f"The factorial of 5 : {factorial(5)}")
print(f"The factorial of 10: {factorial(10)}")
print("-" * 36)
print()

# Interactive test for user input
user_num = int(input("Enter a non-negative integer to find its factorial: "))
print()

result = factorial(user_num)

print("====================================")
print("========== RESULT SUMMARY ==========")
print("====================================")
print(f"Number provided : {user_num}")
print(f"Factorial result: {result}")
print("====================================")