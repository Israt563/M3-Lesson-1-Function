# Math Module Explorer
# File  : math_explorer.py

import math

print("====================================")
print("      Welcome to Math Explorer!     ")
print("====================================")
print()

# 1. Floor and Ceil demonstration
print("--- 1. Ceil & Floor Functions ---")
val = 23.56
print(f"Original value : {val}")
print(f"Ceiling value  : {math.ceil(val)}")
print(f"Floor value    : {math.floor(val)}")
print()

# 2. Copysign demonstration
print("--- 2. Copy Sign Function ---")
x = 10
y = -15
new_x = math.copysign(x, y)
print(f"x = {x}, y = {y}")
print(f"Value of x after copying sign from y : {new_x}")
print()

# 3. Absolute value demonstration (fabs)
print("--- 3. Absolute Value (fabs) ---")
print(f"Absolute value of -96 : {math.fabs(-96)}")
print(f"Absolute value of 56  : {math.fabs(56)}")
print()

# 4. GCD demonstration
print("--- 4. Greatest Common Divisor (GCD) ---")
a, b = 24, 56
print(f"The GCD of {a} and {b} : {math.gcd(a, b)}")
print("-" * 36)
print()

# 5. Interactive bonus test for the user
print("--- Bonus: Try Your Own Decimal! ---")
try:
    user_num = float(input("Enter any decimal number (e.g., 7.8): "))
    print()
    print(f"Ceiling of {user_num} : {math.ceil(user_num)}")
    print(f"Floor of {user_num}   : {math.floor(user_num)}")
except ValueError:
    print("Oops! That wasn't a valid number.")

print()
print("====================================")
print("   Math module exploration complete! 📐")
print("====================================")