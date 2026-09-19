# Safe Division Calculator with Multiple Exceptions
# File  : safe_division.py

print("====================================")
print("   Welcome to Safe Division Calc!   ")
print("====================================")
print()

try:
    # Using eval to catch missing commas or syntax errors
    num1, num2 = eval(input("Enter two numbers, separated by a comma (e.g., 10, 2): "))
    result = num1 / num2
    print()
    print(f"Success! Result is: {result}")

# Using multiple except blocks for different types of errors
except ZeroDivisionError:
    print()
    print("❌ Error: Division by zero is not allowed!")

except SyntaxError:
    print()
    print("❌ Error: Comma is missing. Enter numbers separated by a comma like this: 10, 2")

except Exception as ex:
    print()
    print(f"❌ Wrong input or unexpected error: {ex}")

else:
    print()
    print("✨ No exceptions occurred during calculation!")

finally:
    print()
    print("🔒 [Finally Block]: This will execute no matter what.")

print()
print("====================================")
print("   Calculation session ended. 🧮    ")
print("====================================")