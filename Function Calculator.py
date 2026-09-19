# Function Calculator Program
# File  : function_calculator.py

print("====================================")
print("   Welcome to Function Calculator!  ")
print("====================================")
print()

# PART 1: Define the four calculation functions using def and return
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b

# PART 2: Display operation choices to the user
print("Select an operation:")
print("  + : Addition")
print("  - : Subtraction")
print("  * : Multiplication")
print("  / : Division")
print("-" * 36)
print()

# PART 3: Get user input and execute calculation with error handling
try:
    op = input("Enter operation (+, -, *, /): ").strip()
    
    if op not in ['+', '-', '*', '/']:
        print()
        print("❌ Error: Invalid operation selected. Please choose +, -, *, or /.")
    else:
        num1 = float(input("Enter the first number : "))
        num2 = float(input("Enter the second number: "))
        print()
        
        # PART 4: Call the correct function based on the operation
        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)
            
        # PART 5: Print the final result cleanly
        print("====================================")
        print("========== RESULT SUMMARY ==========")
        print("====================================")
        print(f"Expression : {num1} {op} {num2}")
        print(f"Result     : {result}")
        print("====================================")

except ZeroDivisionError:
    print()
    print("❌ Error: Division by zero is not allowed!")

except ValueError:
    print()
    print("❌ Error: Invalid input! Please enter valid numeric values.")

except Exception as ex:
    print()
    print(f"❌ An unexpected error occurred: {ex}")

print()
print("====================================")
print("   Calculation session finished! 🧮 ")
print("====================================")