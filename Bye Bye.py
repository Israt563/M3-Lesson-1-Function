# Even Number Validator with Nested Loops & Error Handling
# File  : even_validator.py

print("====================================")
print("    Welcome to Even Number Checker! ")
print("====================================")
print()

valid = False

# Outer while loop for input validation (catches letters/symbols)
while not valid: 
    try:
        n = int(input("Enter an even number: "))
        print()
        
        # Nested while loop to handle the even number condition
        while n % 2 == 0:
            print(f"Success! {n} is an even number. 👋 Bye!")
            break  # Break prevents an infinite loop here!
            
        # If it was an odd number, let the user know and prompt again
        if n % 2 != 0:
            print(f"⚠️ {n} is odd. We wanted an even number! Try again.\n")
            continue
            
        valid = True
        
    except ValueError:
        print("❌ Invalid input! Please enter a valid whole number.\n")

print()
print("====================================")
print("   Validation completed successfully! 🎉")
print("====================================")