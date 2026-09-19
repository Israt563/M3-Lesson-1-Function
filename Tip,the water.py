# Tip Calculator Program
# File  : tip_calculator.py

print("====================================")
print("      Welcome to Tip Calculator!    ")
print("====================================")
print()

# Define function to calculate the tip on a bill with a default tip percentage of 15%
def total_calc(bill_amount, tip_perc=15):
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print(f"Bill Amount : ${bill_amount:.2f}")
    print(f"Tip Percent : {tip_perc}%")
    print(f"Total to Pay: ${total:.2f}")
    print("-" * 36)

# Test 1: Using only the bill amount (default tip percentage of 15% is used)
print("--- Test 1: Default Tip ---")
total_calc(150)
print()

# Test 2: Specifying both bill amount and a custom tip percentage
print("--- Test 2: Custom Tip ---")
total_calc(150, 20)

print()
print("====================================")
print("   Calculation complete! 💸         ")
print("====================================")